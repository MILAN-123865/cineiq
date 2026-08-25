"""Synchronise the local catalogue with TMDB and seed verified offline movies if empty."""

from datetime import datetime
import httpx
import structlog
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.db.models import Movie

logger = structlog.get_logger()

GENRE_MAP = {
    28: "Action", 12: "Adventure", 16: "Animation", 35: "Comedy",
    80: "Crime", 99: "Documentary", 18: "Drama", 10751: "Family",
    14: "Fantasy", 36: "History", 27: "Horror", 10402: "Music",
    9648: "Mystery", 10749: "Romance", 878: "Sci-Fi", 10770: "TV Movie",
    53: "Thriller", 10752: "War", 37: "Western",
}

OFFLINE_SEED_MOVIES = [
    {
        "id": "1",
        "title": "Interstellar",
        "overview": "When Earth becomes uninhabitable in the future, a farmer and ex-NASA pilot, Joseph Cooper, is tasked to pilot a spacecraft to find a new home for humans.",
        "release_date": datetime(2014, 11, 7),
        "poster_path": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/xJHokMbljvjADYdit5fK5VQsXEG.jpg",
        "genres": ["Adventure", "Drama", "Sci-Fi"],
        "popularity": 145.2,
        "vote_average": 8.7,
        "vote_count": 34500,
        "dominant_emotion": "Awe-Inspiring",
        "emotional_arc": [
            {"time": "0m", "tension": 15, "awe": 20, "action": 5},
            {"time": "40m", "tension": 45, "awe": 70, "action": 30},
            {"time": "80m", "tension": 85, "awe": 90, "action": 65},
            {"time": "120m", "tension": 95, "awe": 98, "action": 90},
            {"time": "160m", "tension": 40, "awe": 100, "action": 20}
        ]
    },
    {
        "id": "2",
        "title": "Inception",
        "overview": "Cobb steals information from his targets by entering their dreams. He is offered a chance to regain his old life as payment for a task considered impossible: inception.",
        "release_date": datetime(2010, 7, 16),
        "poster_path": "https://image.tmdb.org/t/p/w500/oYuLEt3zVCKq57qu2F8dT7NIa6f.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/8ZTVqvKDQ8emSGUEMjsS4yHAwrp.jpg",
        "genres": ["Action", "Adventure", "Sci-Fi", "Thriller"],
        "popularity": 135.8,
        "vote_average": 8.8,
        "vote_count": 36000,
        "dominant_emotion": "Mind-Bending",
        "emotional_arc": [
            {"time": "0m", "tension": 30, "awe": 40, "action": 25},
            {"time": "35m", "tension": 50, "awe": 65, "action": 40},
            {"time": "70m", "tension": 75, "awe": 80, "action": 60},
            {"time": "105m", "tension": 90, "awe": 92, "action": 85},
            {"time": "140m", "tension": 98, "awe": 95, "action": 90}
        ]
    },
    {
        "id": "3",
        "title": "Dune: Part Two",
        "overview": "Paul Atreides unites with Chani and the Fremen while seeking revenge against the conspirators who destroyed his family.",
        "release_date": datetime(2024, 3, 1),
        "poster_path": "https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2JGqpTd4p.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/xOMo8BRK7PfcJv9JCnx7s520b22.jpg",
        "genres": ["Action", "Adventure", "Drama", "Sci-Fi"],
        "popularity": 180.5,
        "vote_average": 8.6,
        "vote_count": 8500,
        "dominant_emotion": "Epic Thrill",
        "emotional_arc": [
            {"time": "0m", "tension": 40, "awe": 50, "action": 30},
            {"time": "40m", "tension": 60, "awe": 80, "action": 50},
            {"time": "80m", "tension": 75, "awe": 90, "action": 70},
            {"time": "120m", "tension": 90, "awe": 95, "action": 85},
            {"time": "160m", "tension": 98, "awe": 100, "action": 95}
        ]
    },
    {
        "id": "4",
        "title": "Oppenheimer",
        "overview": "The story of J. Robert Oppenheimer's role in the development of the atomic bomb during World War II.",
        "release_date": datetime(2023, 7, 21),
        "poster_path": "https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/fm6KqXpk3M2HVveHwCrBSSBaO0V.jpg",
        "genres": ["Biography", "Drama", "History"],
        "popularity": 160.0,
        "vote_average": 8.9,
        "vote_count": 14000,
        "dominant_emotion": "Tense & Gripping",
        "emotional_arc": [
            {"time": "0m", "tension": 20, "awe": 30, "action": 10},
            {"time": "45m", "tension": 50, "awe": 60, "action": 20},
            {"time": "90m", "tension": 80, "awe": 85, "action": 40},
            {"time": "135m", "tension": 100, "awe": 98, "action": 80},
            {"time": "175m", "tension": 85, "awe": 90, "action": 30}
        ]
    },
    {
        "id": "5",
        "title": "The Dark Knight",
        "overview": "When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological tests of his ability to fight injustice.",
        "release_date": datetime(2008, 7, 18),
        "poster_path": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/dqK9Hag1054tghRQSqLSfrkvQnA.jpg",
        "genres": ["Action", "Crime", "Drama", "Thriller"],
        "popularity": 150.0,
        "vote_average": 9.0,
        "vote_count": 32000,
        "dominant_emotion": "High Adrenaline",
        "emotional_arc": [
            {"time": "0m", "tension": 50, "awe": 40, "action": 60},
            {"time": "40m", "tension": 70, "awe": 60, "action": 75},
            {"time": "80m", "tension": 85, "awe": 70, "action": 80},
            {"time": "120m", "tension": 95, "awe": 85, "action": 95},
            {"time": "150m", "tension": 90, "awe": 90, "action": 85}
        ]
    },
    {
        "id": "6",
        "title": "Spirited Away",
        "overview": "During her family's move to the suburbs, a sullen 10-year-old girl wanders into a world ruled by gods, witches, and spirits.",
        "release_date": datetime(2001, 7, 20),
        "poster_path": "https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/mSDsSDwaP3E7dEfUPWy4J0djt4O.jpg",
        "genres": ["Animation", "Adventure", "Family", "Fantasy"],
        "popularity": 110.0,
        "vote_average": 8.6,
        "vote_count": 16500,
        "dominant_emotion": "Magical Wonder",
        "emotional_arc": [
            {"time": "0m", "tension": 20, "awe": 30, "action": 10},
            {"time": "30m", "tension": 40, "awe": 60, "action": 25},
            {"time": "60m", "tension": 65, "awe": 85, "action": 40},
            {"time": "90m", "tension": 70, "awe": 95, "action": 35},
            {"time": "120m", "tension": 30, "awe": 100, "action": 15}
        ]
    },
    {
        "id": "7",
        "title": "Spider-Man: Across the Spider-Verse",
        "overview": "Miles Morales catapults across the Multiverse, where he encounters a team of Spider-People charged with protecting its very existence.",
        "release_date": datetime(2023, 6, 2),
        "poster_path": "https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/4HodYYKEIsGOdinkGi2Ucz6X9i0.jpg",
        "genres": ["Action", "Adventure", "Animation", "Sci-Fi"],
        "popularity": 170.0,
        "vote_average": 8.7,
        "vote_count": 14200,
        "dominant_emotion": "Mind-Bending Action",
        "emotional_arc": [
            {"time": "0m", "tension": 35, "awe": 50, "action": 40},
            {"time": "35m", "tension": 55, "awe": 75, "action": 60},
            {"time": "70m", "tension": 80, "awe": 90, "action": 85},
            {"time": "105m", "tension": 95, "awe": 98, "action": 95},
            {"time": "135m", "tension": 90, "awe": 95, "action": 80}
        ]
    },
    {
        "id": "8",
        "title": "Parasite",
        "overview": "Greed and class discrimination threaten the newly formed symbiotic relationship between the wealthy Park family and the destitute Kim clan.",
        "release_date": datetime(2019, 5, 30),
        "poster_path": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg",
        "backdrop_path": "https://image.tmdb.org/t/p/original/hiKmpZMGZsrkA3cdce8a7Dpos1j.jpg",
        "genres": ["Comedy", "Drama", "Thriller"],
        "popularity": 125.0,
        "vote_average": 8.5,
        "vote_count": 18000,
        "dominant_emotion": "Tense Suspense",
        "emotional_arc": [
            {"time": "0m", "tension": 10, "awe": 20, "action": 5},
            {"time": "30m", "tension": 30, "awe": 40, "action": 15},
            {"time": "65m", "tension": 70, "awe": 60, "action": 40},
            {"time": "95m", "tension": 95, "awe": 80, "action": 75},
            {"time": "130m", "tension": 90, "awe": 85, "action": 50}
        ]
    }
]


async def seed_movies_if_empty(db: AsyncSession) -> None:
    """Seed initial movies on startup so the catalog is never empty for contributors."""
    if (await db.execute(select(Movie.id).limit(1))).scalar_one_or_none():
        return

    # If TMDB is configured, try live sync
    if settings.tmdb_api_key and "placeholder" not in settings.tmdb_api_key.lower():
        try:
            movies: dict[str, Movie] = {}
            async with httpx.AsyncClient(timeout=10.0) as client:
                for endpoint in ("movie/popular", "trending/movie/day"):
                    try:
                        response = await client.get(
                            f"https://api.themoviedb.org/3/{endpoint}",
                            params={"language": "en-US", "page": 1},
                            headers={"Authorization": f"Bearer {settings.tmdb_api_key}", "accept": "application/json"},
                        )
                        response.raise_for_status()
                    except Exception as err:
                        logger.warning("tmdb_sync_partial_error", error=str(err))
                        continue

                    for item in response.json().get("results", []):
                        movie_id = str(item.get("id", ""))
                        if not movie_id or movie_id in movies:
                            continue
                        rel_date = None
                        if item.get("release_date"):
                            try:
                                rel_date = datetime.strptime(item["release_date"], "%Y-%m-%d")
                            except ValueError:
                                pass
                        movies[movie_id] = Movie(
                            id=movie_id,
                            title=item.get("title") or "Untitled",
                            overview=item.get("overview") or "",
                            release_date=rel_date,
                            poster_path=(f"https://image.tmdb.org/t/p/w500{item['poster_path']}" if item.get("poster_path") else None),
                            backdrop_path=(f"https://image.tmdb.org/t/p/original{item['backdrop_path']}" if item.get("backdrop_path") else None),
                            genres=[GENRE_MAP[gid] for gid in item.get("genre_ids", []) if gid in GENRE_MAP],
                            popularity=float(item.get("popularity") or 0),
                            vote_average=float(item.get("vote_average") or 0),
                            vote_count=int(item.get("vote_count") or 0),
                            dominant_emotion="Thrilling",
                            emotional_arc=[{"time": "0m", "tension": 20, "awe": 30, "action": 10}, {"time": "60m", "tension": 70, "awe": 80, "action": 60}, {"time": "120m", "tension": 95, "awe": 90, "action": 85}],
                        )
            if movies:
                db.add_all(movies.values())
                await db.commit()
                logger.info("tmdb_catalogue_seeded", count=len(movies))
                return
        except Exception as e:
            logger.warning("tmdb_sync_failed_using_offline_seed", error=str(e))

    # Automatic offline seed fallback for all contributors
    seed_objects = [
        Movie(
            id=item["id"],
            title=item["title"],
            overview=item["overview"],
            release_date=item["release_date"],
            poster_path=item["poster_path"],
            backdrop_path=item["backdrop_path"],
            genres=item["genres"],
            popularity=item["popularity"],
            vote_average=item["vote_average"],
            vote_count=item["vote_count"],
            dominant_emotion=item["dominant_emotion"],
            emotional_arc=item["emotional_arc"],
        )
        for item in OFFLINE_SEED_MOVIES
    ]
    db.add_all(seed_objects)
    await db.commit()
    logger.info("offline_verified_catalogue_seeded", count=len(seed_objects))
