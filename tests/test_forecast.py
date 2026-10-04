from fastapi.testclient import TestClient
from capacity.main import app

client = TestClient(app)


def test_moving_average():
    payload = client.post("/forecast", json={"series": [50, 55, 60, 65]}).json()
    assert payload["next"] == 60.0


def test_short_series_is_refused():
    assert client.post("/forecast", json={"series": [1]}).status_code == 422
