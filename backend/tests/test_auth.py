import pytest
from httpx import ASGITransport, AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_protected_endpoint_without_token_fails():
    """Verify that accessing protected endpoints without auth token returns 401/403 or 503."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/v1/profile/stats")
        assert response.status_code in (401, 403, 503)

@pytest.mark.asyncio
async def test_room_create_unauthenticated_fails():
    """Verify that creating a watch room without auth token returns 401/403 or 503."""
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/v1/room/create")
        assert response.status_code in (401, 403, 503)
