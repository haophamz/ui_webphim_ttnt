"""
models.py
----------
Định nghĩa các bảng database cho module N4 (Episodes Module).

Theo tài liệu nhiệm vụ N4:
    Movie (1) ------ (N) Episode
    Episode được User xem -> ghi vào WatchHistory
    WatchHistory chính là dữ liệu đầu vào cho hệ thống Recommendation (AI).
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Movie(db.Model):
    """Bảng Movie - thông tin chung của 1 bộ phim.

    Lưu ý: bảng này có thể được N2/N3 quản lý chi tiết hơn (poster, mô tả,
    thể loại...). Ở đây N4 chỉ định nghĩa tối thiểu để Episode có thể
    tham chiếu (foreign key) và để demo độc lập module N4.
    """

    __tablename__ = "movie"

    movie_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, default="")
    poster = db.Column(db.String(500), default="")

    episodes = db.relationship(
        "Episode",
        backref="movie",
        order_by="Episode.episode_number",
        cascade="all, delete-orphan",
    )

    def to_dict(self):
        return {
            "movie_id": self.movie_id,
            "title": self.title,
            "description": self.description,
            "poster": self.poster,
            "total_episodes": len(self.episodes),
        }


class Episode(db.Model):
    """Bảng Episode - mỗi dòng là 1 tập phim thuộc về 1 Movie."""

    __tablename__ = "episode"

    episode_id = db.Column(db.Integer, primary_key=True)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    episode_number = db.Column(db.Integer, nullable=False)
    episode_name = db.Column(db.String(255), default="")
    video_url = db.Column(db.String(500), nullable=False)

    __table_args__ = (
        db.UniqueConstraint("movie_id", "episode_number", name="uq_movie_episode"),
    )

    def to_dict(self):
        return {
            "episode_id": self.episode_id,
            "movie_id": self.movie_id,
            "episode_number": self.episode_number,
            "episode_name": self.episode_name,
            "video_url": self.video_url,
        }


class WatchHistory(db.Model):
    """Bảng WatchHistory - lưu lại mỗi lần user xem 1 tập phim.

    Đây là dữ liệu N4 cung cấp cho hệ thống AI Recommendation của nhóm
    (ví dụ: nhóm AI sẽ query bảng này để biết user thích thể loại nào,
    xem đến tập nào, từ đó gợi ý phim tiếp theo).
    """

    __tablename__ = "watch_history"

    history_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    episode_id = db.Column(db.Integer, db.ForeignKey("episode.episode_id"), nullable=False)
    watched_at = db.Column(db.DateTime, server_default=db.func.now())

    def to_dict(self):
        return {
            "history_id": self.history_id,
            "user_id": self.user_id,
            "movie_id": self.movie_id,
            "episode_id": self.episode_id,
            "watched_at": self.watched_at.isoformat() if self.watched_at else None,
        }
