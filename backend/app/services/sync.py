import structlog
import httpx
from datetime import datetime
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.config import settings
from app.db.models import Movie

logger = structlog.get_logger()

# Standard TMDB Genre ID to Name Mapping
GENRE_MAP = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    99: "Documentary",
    18: "Drama",
    10751: "Family",
    14: "Fantasy",
    36: "History",
    27: "Horror",
    10402: "Music",
    9648: "Mystery",
    10749: "Romance",
    878: "Sci-Fi",
    10770: "TV Movie",
    53: "Thriller",
    10752: "War",
    37: "Western"
}

# Some mock emotional arcs to seed into database
MOCK_EMOTIONAL_ARCS = [
    [
        {"time": "0m", "tension": 10, "awe": 20, "action": 5},
        {"time": "30m", "tension": 40, "awe": 50, "action": 30},
        {"time": "60m", "tension": 60, "awe": 45, "action": 55},
        {"time": "90m", "tension": 85, "awe": 70, "action": 80},
        {"time": "120m", "tension": 50, "awe": 90, "action": 20}
    ],
    [
        {"time": "0m", "tension": 30, "awe": 40, "action": 10},
        {"time": "30m", "tension": 45, "awe": 60, "action": 20},
        {"time": "60m", "tension": 80, "awe": 50, "action": 75},
        {"time": "90m", "tension": 60, "awe": 85, "action": 40},
        {"time": "120m", "tension": 95, "awe": 70, "action": 90},
        {"time": "150m", "tension": 100, "awe": 95, "action": 100},
        {"time": "166m", "tension": 40, "awe": 100, "action": 20}
    ],
    [
        {"time": "0m", "tension": 5, "awe": 10, "action": 2},
        {"time": "30m", "tension": 15, "awe": 30, "action": 10},
        {"time": "60m", "tension": 35, "awe": 40, "action": 15},
        {"time": "90m", "tension": 70, "awe": 55, "action": 45},
        {"time": "120m", "tension": 20, "awe": 80, "action": 10}
    ]
]

MOCK_DOMINANT_EMOTIONS = ["Tense", "Inspiring", "Heartwarming", "Thrilling", "Melancholic", "Mind-bending"]

async def seed_movies_if_empty(db: AsyncSession):
    """Seed movies from TMDB popular & trending lists if DB is empty."""
    # Check if we already have movies
    stmt = select(Movie).limit(1)
    result = await db.execute(stmt)
    if result.scalars().first():
        logger.info("sync_db_not_empty_skipping_seed")
        return

    logger.info("sync_db_empty_starting_seed")

    # If TMDB key is a placeholder or missing, seed a fallback set
    if not settings.tmdb_api_key or "placeholder" in settings.tmdb_api_key.lower():
        logger.warning("sync_tmdb_key_missing_using_fallbacks")
        await _seed_fallback_movies(db)
        return

    # Fetch from TMDB
    endpoints = ["movie/popular", "trending/movie/day"]
    seen_ids = set()
    movies_to_insert = []

    async with httpx.AsyncClient() as client:
        for endpoint in endpoints:
            try:
                resp = await client.get(
                    f"https://api.themoviedb.org/3/{endpoint}",
                    params={"language": "en-US", "page": 1},
                    headers={
                        "Authorization": f"Bearer {settings.tmdb_api_key}",
                        "accept": "application/json"
                    },
                    timeout=15.0
                )
                if resp.status_code == 200:
                    results = resp.json().get("results", [])
                    for item in results:
                        movie_id = str(item.get("id"))
                        if movie_id in seen_ids:
                            continue
                        seen_ids.add(movie_id)

                        # Parse genres
                        genre_ids = item.get("genre_ids", [])
                        genres = [GENRE_MAP.get(gid, "Drama") for gid in genre_ids if gid in GENRE_MAP]
                        if not genres:
                            genres = ["Movie"]

                        # Parse date
                        release_date_str = item.get("release_date")
                        release_date = None
                        if release_date_str:
                            try:
                                release_date = datetime.strptime(release_date_str, "%Y-%m-%d")
                            except ValueError:
                                pass

                        import random
                        movie_obj = Movie(
                            id=movie_id,
                            title=item.get("title", "Unknown Title"),
                            overview=item.get("overview", ""),
                            release_date=release_date,
                            poster_path=f"https://image.tmdb.org/t/p/w500{item.get('poster_path')}" if item.get("poster_path") else None,
                            backdrop_path=f"https://image.tmdb.org/t/p/original{item.get('backdrop_path')}" if item.get("backdrop_path") else None,
                            genres=genres,
                            popularity=float(item.get("popularity", 0.0)),
                            vote_average=float(item.get("vote_average", 0.0)),
                            vote_count=int(item.get("vote_count", 0)),
                            dominant_emotion=random.choice(MOCK_DOMINANT_EMOTIONS),
                            emotional_arc=random.choice(MOCK_EMOTIONAL_ARCS)
                        )
                        movies_to_insert.append(movie_obj)
            except Exception as e:
                logger.error("sync_tmdb_fetch_error", endpoint=endpoint, error=str(e))

    if movies_to_insert:
        try:
            db.add_all(movies_to_insert)
            await db.commit()
            logger.info("sync_db_seeded_successfully", count=len(movies_to_insert))
        except Exception as e:
            await db.rollback()
            logger.error("sync_db_save_failed", error=str(e))
    else:
        # Fallback if no movies fetched
        await _seed_fallback_movies(db)

async def _seed_fallback_movies(db: AsyncSession):
    """Seed high-quality fallbacks if TMDB is unreachable/not configured."""
    fallbacks = [
        Movie(
            id="1",
            title="Dune: Part Two",
            overview="Paul Atreides unites with Chani and the Fremen while on a warpath of revenge against the conspirators who destroyed his family.",
            release_date=datetime(2024, 3, 1),
            poster_path="https://image.tmdb.org/t/p/w500/1pdfLvkbY9ohJlCjQH2JGqpTd4p.jpg",
            backdrop_path="https://image.tmdb.org/t/p/original/8rpDcsfLJypbO6vtecsmHLsC88C.jpg",
            genres=["Sci-Fi", "Adventure"],
            popularity=1200.5,
            vote_average=8.3,
            vote_count=3500,
            dominant_emotion="Tense",
            emotional_arc=MOCK_EMOTIONAL_ARCS[1]
        ),
        Movie(
            id="2",
            title="Oppenheimer",
            overview="The story of American scientist J. Robert Oppenheimer and his role in the development of the atomic bomb.",
            release_date=datetime(2023, 7, 21),
            poster_path="https://image.tmdb.org/t/p/w500/8Gxv8gSFCU0XGDykEGv7zR1n2ua.jpg",
            backdrop_path="https://image.tmdb.org/t/p/original/fm6k40xrWg2jCu2eTI4EsTAaN0n.jpg",
            genres=["Drama", "History"],
            popularity=850.2,
            vote_average=8.1,
            vote_count=7200,
            dominant_emotion="Inspiring",
            emotional_arc=MOCK_EMOTIONAL_ARCS[0]
        ),
        Movie(
            id="3",
            title="Poor Things",
            overview="The incredible tale and fantastical evolution of Bella Baxter, a young woman brought back to life by the brilliant and unorthodox scientist Dr. Godwin Baxter.",
            release_date=datetime(2023, 12, 8),
            poster_path="https://image.tmdb.org/t/p/w500/kCGlIMHnOm8PhcbTi03XQ5VGe1T.jpg",
            backdrop_path="https://image.tmdb.org/t/p/original/9w0McGip6JA85g7H557i4TN7a5c.jpg",
            genres=["Comedy", "Fantasy", "Sci-Fi"],
            popularity=620.1,
            vote_average=7.8,
            vote_count=2900,
            dominant_emotion="Mind-bending",
            emotional_arc=MOCK_EMOTIONAL_ARCS[2]
        ),
        Movie(
            id="4",
            title="Interstellar",
            overview="A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
            release_date=datetime(2014, 11, 7),
            poster_path="https://image.tmdb.org/t/p/w500/gEU2QlsE1ZEbKU01E8XgK31rGfQ.jpg",
            backdrop_path="https://image.tmdb.org/t/p/original/rAiWn0v67w4vUaL062aq36R8Jt0.jpg",
            genres=["Adventure", "Sci-Fi", "Drama"],
            popularity=540.4,
            vote_average=8.4,
            vote_count=32000,
            dominant_emotion="Mind-bending",
            emotional_arc=MOCK_EMOTIONAL_ARCS[0]
        ),
        Movie(
            id="5",
            title="Inception",
            overview="Cobb, a skilled thief who steals valuable secrets from deep within the subconscious during the dream state, is given a chance to have his life back.",
            release_date=datetime(2010, 7, 16),
            poster_path="https://image.tmdb.org/t/p/w500/oYuLEt3zVCKqA3F0B7I2G0kE7Y.jpg",
            backdrop_path="https://image.tmdb.org/t/p/original/s3Tzczdf3UE89WHSVTMK2FJZ1cc.jpg",
            genres=["Action", "Sci-Fi", "Adventure"],
            popularity=490.8,
            vote_average=8.4,
            vote_count=35000,
            dominant_emotion="Thrilling",
            emotional_arc=MOCK_EMOTIONAL_ARCS[1]
        ),
        Movie(
            id="6",
            title="Arrival",
            overview="Taking place after mysterious spacecraft touch down across the globe, an elite team is put together to investigate.",
            release_date=datetime(2016, 11, 11),
            poster_path="https://image.tmdb.org/t/p/w500/x2FJsf1ElAgr63Y3PNPtJrcmpoe.jpg",
            backdrop_path="https://image.tmdb.org/t/p/original/71tN7a4Hk9R4Q5F3C28L9PzS7Z5.jpg",
            genres=["Drama", "Sci-Fi", "Mystery"],
            popularity=320.6,
            vote_average=7.6,
            vote_count=16000,
            dominant_emotion="Mind-bending",
            emotional_arc=MOCK_EMOTIONAL_ARCS[2]
        )
    ]
    try:
        db.add_all(fallbacks)
        await db.commit()
        logger.info("sync_db_fallback_seeded", count=len(fallbacks))
    except Exception as e:
        await db.rollback()
        logger.error("sync_db_fallback_failed", error=str(e))
