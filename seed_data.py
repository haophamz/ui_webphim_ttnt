"""
seed_data.py
------------
Chèn dữ liệu mẫu vào database để demo module N4 độc lập
(trong lúc chưa tích hợp với database thật của N2/N3).

Chạy: python seed_data.py
"""

from app import create_app
from models import db, Movie, Episode

SAMPLE_VIDEO = "https://www.w3schools.com/html/mov_bbb.mp4"  # video mẫu để test player

MOVIES = [
    {
        "title": "Demo 1",
        "description": "Phim demo số 1 — sẽ được cập nhật khi nhóm hoàn thành tích hợp.",
        "poster": "",
        "episode_count": 6,
    },
    {
        "title": "Demo 2",
        "description": "Phim demo số 2 — sẽ được cập nhật khi nhóm hoàn thành tích hợp.",
        "poster": "",
        "episode_count": 4,
    },
]


def seed():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        for movie_data in MOVIES:
            movie = Movie(
                title=movie_data["title"],
                description=movie_data["description"],
                poster=movie_data["poster"],
            )
            db.session.add(movie)
            db.session.flush()  # để có movie.movie_id trước khi tạo Episode

            for i in range(1, movie_data["episode_count"] + 1):
                ep = Episode(
                    movie_id=movie.movie_id,
                    episode_number=i,
                    episode_name=f"{movie_data['title']} - Tập {i}",
                    video_url=SAMPLE_VIDEO,
                )
                db.session.add(ep)

        db.session.commit()
        print("Seed dữ liệu mẫu thành công!")
        for m in Movie.query.all():
            print(f"  - movie_id={m.movie_id} | {m.title} | {len(m.episodes)} tập")


if __name__ == "__main__":
    seed()
