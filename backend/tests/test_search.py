from fastapi.testclient import TestClient
from app.main import app

def test_search_endpoint_returns_results():
    """Verify that semantic search endpoint handles queries and returns result list."""
    client = TestClient(app)
    response = client.get("/api/v1/search/semantic?q=Interstellar")
    assert response.status_code == 200
    data = response.json()
    assert "query" in data
    assert "results" in data
    assert isinstance(data["results"], list)

def test_search_missing_query_fails():
    """Verify that semantic search without 'q' returns validation error 422."""
    client = TestClient(app)
    response = client.get("/api/v1/search/semantic")
    assert response.status_code == 422
