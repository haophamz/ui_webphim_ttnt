"""
app.py
------
Flask app cho module N4 - Episodes Module (Tập phim).

Các chức năng đã triển khai theo đúng yêu cầu N4:
    1. Hiển thị danh sách tập phim       -> GET  /movie/<movie_id>
    2. Xem tập phim                      -> GET  /watch/<movie_id>/<episode_number>
    3. Đánh dấu tập đang xem              -> xử lý trong template watch.html
    4. Chuyển tập trước / tập sau         -> xử lý trong template watch.html
    5. Lưu lịch sử xem (cho AI gợi ý)     -> tự động ghi log khi vào /watch/...

API public cho các module khác (N1-N5) / nhóm AI sử dụng:
    GET  /api/movies/<movie_id>/episodes   -> danh sách tập (JSON)
    GET  /api/watch-history                -> toàn bộ lịch sử xem (JSON, cho AI)
    GET  /api/watch-history/<user_id>      -> lịch sử xem của 1 user (JSON)

Lưu ý tích hợp với N5 (đăng nhập):
    Hiện tại chưa có hệ thống login thật nên mình dùng session đơn giản,
    mặc định user_id = 1 (guest). Khi N5 hoàn thành module login, chỉ cần
    thay current_user_id() bên dưới để lấy user_id thật từ session đăng nhập.
"""

import os

from flask import Flask, render_template, redirect, url_for, jsonify, session, abort

from models import db, Movie, Episode, WatchHistory

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "movie_app.db")


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = "n4-episodes-dev-secret"  # đổi khi deploy thật

    db.init_app(app)
    return app


app = create_app()


def current_user_id():
    """Lấy user_id hiện tại.

    TODO (tích hợp với N5): khi có login thật, thay đoạn này bằng
    session.get('user_id') được set lúc N5 xác thực đăng nhập thành công.
    Hiện tại mặc định user_id = 1 để demo module N4 độc lập.
    """
    return session.get("user_id", 1)


# ---------------------------------------------------------------------------
# Trang chủ demo (chỉ phục vụ test, N2 sẽ làm trang danh sách phim thật)
# ---------------------------------------------------------------------------
@app.route("/")
def index():
    movies = Movie.query.all()
    return render_template("index.html", movies=movies)


# ---------------------------------------------------------------------------
# Chức năng 1: Hiển thị danh sách tập phim
# ---------------------------------------------------------------------------
@app.route("/movie/<int:movie_id>")
def movie_detail(movie_id):
    movie = Movie.query.get_or_404(movie_id)
    episodes = (
        Episode.query.filter_by(movie_id=movie_id)
        .order_by(Episode.episode_number)
        .all()
    )
    return render_template("movie_detail.html", movie=movie, episodes=episodes)


# ---------------------------------------------------------------------------
# Chức năng 2, 3, 4: Xem tập phim + đánh dấu tập đang xem + chuyển tập trước/sau
# Chức năng 5: Lưu lịch sử xem
# ---------------------------------------------------------------------------
@app.route("/watch/<int:movie_id>/<int:episode_number>")
def watch_episode(movie_id, episode_number):
    movie = Movie.query.get_or_404(movie_id)
    episode = Episode.query.filter_by(
        movie_id=movie_id, episode_number=episode_number
    ).first()
    if episode is None:
        abort(404)

    all_episodes = (
        Episode.query.filter_by(movie_id=movie_id)
        .order_by(Episode.episode_number)
        .all()
    )

    prev_episode = next(
        (e for e in reversed(all_episodes) if e.episode_number < episode_number), None
    )
    next_episode = next(
        (e for e in all_episodes if e.episode_number > episode_number), None
    )

    # Chức năng 5: Lưu lịch sử xem ngay khi user mở trang xem tập phim
    log_watch_history(user_id=current_user_id(), movie_id=movie_id, episode_id=episode.episode_id)

    return render_template(
        "watch.html",
        movie=movie,
        episode=episode,
        all_episodes=all_episodes,
        prev_episode=prev_episode,
        next_episode=next_episode,
    )


def log_watch_history(user_id, movie_id, episode_id):
    """Ghi lại lịch sử xem -> dữ liệu đầu vào cho hệ thống Recommendation (AI)."""
    history = WatchHistory(user_id=user_id, movie_id=movie_id, episode_id=episode_id)
    db.session.add(history)
    db.session.commit()


# ---------------------------------------------------------------------------
# API cho các module khác / nhóm AI sử dụng
# ---------------------------------------------------------------------------
@app.route("/api/movies/<int:movie_id>/episodes")
def api_episode_list(movie_id):
    Movie.query.get_or_404(movie_id)
    episodes = (
        Episode.query.filter_by(movie_id=movie_id)
        .order_by(Episode.episode_number)
        .all()
    )
    return jsonify([e.to_dict() for e in episodes])


@app.route("/api/watch-history")
def api_watch_history_all():
    """Toàn bộ lịch sử xem - nhóm AI dùng để train mô hình gợi ý phim."""
    history = WatchHistory.query.order_by(WatchHistory.watched_at.desc()).all()
    return jsonify([h.to_dict() for h in history])


@app.route("/api/watch-history/<int:user_id>")
def api_watch_history_user(user_id):
    history = (
        WatchHistory.query.filter_by(user_id=user_id)
        .order_by(WatchHistory.watched_at.desc())
        .all()
    )
    return jsonify([h.to_dict() for h in history])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
