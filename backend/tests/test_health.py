from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient
from app.main import app

def test_health_check_healthy():
    """Test health endpoint returns 200 and healthy status when services are ok."""
    mock_redis = MagicMock()
    mock_redis.ping.return_value = True

    with patch("app.db.session.get_redis", return_value=mock_redis):
        client = TestClient(app)
        response = client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "checks" in data
        assert "postgres" in data["checks"]
        assert "redis" in data["checks"]
