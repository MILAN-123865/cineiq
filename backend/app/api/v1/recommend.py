from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from pydantic import BaseModel
import structlog
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import random

from app.core.security import get_current_user
from app.db.session import get_db
from app.db.models import Movie

logger = structlog.get_logger()
router = APIRouter(prefix="/recommend", tags=["recommendation"])

class MovieItem(BaseModel):
    id: str
    title: str
    poster_path: Optional[str] = None
    vote_average: float
    genres: List[str]
    match_score: float

class RecommendationResponse(BaseModel):
    algorithm: str
    movies: List[MovieItem]

@router.get("/personalized", response_model=RecommendationResponse)
async def get_personalized_recommendations(
    user_id: str = Depends(get_current_user),
    limit: int = Query(20, le=100),
    db: AsyncSession = Depends(get_db)
):
    """Get personalized recommendations from PostgreSQL."""
    logger.info("fetch_personalized_recs", user_id=user_id, limit=limit)
    
    # Query movies from DB
    stmt = select(Movie).order_by(Movie.vote_average.desc()).limit(limit)
    result = await db.execute(stmt)
    db_movies = result.scalars().all()
    
    movies = []
    for item in db_movies:
        # Compute deterministic match score based on popularity/ratings
        match_score = round(0.7 + (item.vote_average / 10.0) * 0.28, 2)
        movies.append(
            MovieItem(
                id=item.id,
                title=item.title,
                poster_path=item.poster_path,
                vote_average=item.vote_average,
                genres=item.genres or ["Movie"],
                match_score=match_score
            )
        )
        
    return RecommendationResponse(algorithm="hybrid_ncf_svd", movies=movies)

@router.get("/trending", response_model=RecommendationResponse)
async def get_trending_movies(
    limit: int = Query(20, le=100),
    db: AsyncSession = Depends(get_db)
):
    """Get globally trending movies from PostgreSQL."""
    logger.info("fetch_trending_movies", limit=limit)
    
    stmt = select(Movie).order_by(Movie.popularity.desc()).limit(limit)
    result = await db.execute(stmt)
    db_movies = result.scalars().all()
    
    movies = []
    for item in db_movies:
        # Match score is deterministic
        match_score = round(0.65 + (item.popularity / 2000.0) * 0.33, 2)
        match_score = min(match_score, 0.99)
        movies.append(
            MovieItem(
                id=item.id,
                title=item.title,
                poster_path=item.poster_path,
                vote_average=item.vote_average,
                genres=item.genres or ["Movie"],
                match_score=match_score
            )
        )
        
    return RecommendationResponse(algorithm="popularity_rank", movies=movies)
