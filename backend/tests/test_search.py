import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_search_endpoint_returns_results():
    """Verify that semantic search endpoint handles queries and returns result list."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/search/semantic?q=Interstellar")
        assert response.status_code == 200
        data = response.json()
        assert "query" in data
        assert "results" in data
        assert isinstance(data["results"], list)

@pytest.mark.asyncio
async def test_search_missing_query_fails():
    """Verify that semantic search without 'q' returns validation error 422."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/search/semantic")
        assert response.status_code == 422
