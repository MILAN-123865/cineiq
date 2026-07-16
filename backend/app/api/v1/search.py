from fastapi import APIRouter, Depends, Query
from typing import List, Optional
from pydantic import BaseModel
import structlog
import re
from sqlalchemy import or_
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
import httpx

from app.core.config import settings
from app.db.session import get_db
from app.db.models import Movie

logger = structlog.get_logger()
router = APIRouter(prefix="/search", tags=["search"])

class SearchResult(BaseModel):
    id: str
    title: str
    overview: str
    poster_path: Optional[str] = None
    similarity_score: float

class SearchResponse(BaseModel):
    query: str
    results: List[SearchResult]

@router.get("/semantic", response_model=SearchResponse)
async def semantic_search(
    q: str = Query(..., description="Natural language search query"),
    limit: int = Query(10, le=50),
    db: AsyncSession = Depends(get_db)
):
    """
    Perform semantic search using Google Gemini for intent extraction and local PostgreSQL querying.
    """
    logger.info("semantic_search", query=q, limit=limit)
    
    keywords = q
    
    # 1. Clean query
    cleaned_q = re.sub(r'[^\w\s\-\'"]', '', q).strip()
    
    # 2. Extract keywords using Gemini (if key configured)
    if settings.gemini_api_key and "placeholder" not in settings.gemini_api_key.lower():
        try:
            import google.generativeai as genai
            genai.configure(api_key=settings.gemini_api_key)
            model = genai.GenerativeModel(settings.gemini_model)
            
            prompt = f"""Extract main keywords from this movie search query to be used in a search engine. 
            Return ONLY the keywords separated by spaces.
            Query: "{cleaned_q}"
            """
            
            response = model.generate_content(prompt)
            if response.text:
                extracted = response.text.strip()
                if extracted:
                    keywords = extracted
        except Exception as e:
            logger.warning("gemini_keyword_extraction_failed", error=str(e))

    # 3. Query PostgreSQL using keywords
    words = [w for w in re.split(r'\s+', keywords) if len(w) > 1]
    if not words:
        words = [cleaned_q] if cleaned_q else ["Dune"]

    conditions = []
    for w in words:
        conditions.append(Movie.title.ilike(f"%{w}%"))
        conditions.append(Movie.overview.ilike(f"%{w}%"))

    stmt = select(Movie).where(or_(*conditions)).order_by(Movie.popularity.desc()).limit(limit)
    result = await db.execute(stmt)
    db_movies = result.scalars().all()

    results = []
    for item in db_movies:
        # Simple similarity score calculation based on matching terms
        match_count = sum(1 for w in words if w.lower() in item.title.lower() or w.lower() in item.overview.lower())
        base_score = 0.70 + (match_count / max(len(words), 1)) * 0.25
        similarity_score = round(min(base_score, 0.99), 2)
        
        results.append(
            SearchResult(
                id=item.id,
                title=item.title,
                overview=item.overview,
                poster_path=item.poster_path,
                similarity_score=similarity_score
            )
        )
        
    return SearchResponse(query=q, results=results)
