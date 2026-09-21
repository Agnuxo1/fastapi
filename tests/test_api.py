from datetime import datetime

from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_root_is_accessible_html() -> None:
    response = client.get("/")
    assert response.status_code == 200
    assert "FastAPI Deployment Starter" in response.text


def test_health_and_readiness_are_machine_readable() -> None:
    health = client.get("/api/v1/healthz")
    ready = client.get("/api/v1/readyz")
    assert health.status_code == ready.status_code == 200
    assert health.json()["status"] == "ok"
    assert ready.json()["status"] == "ready"
    assert health.json()["version"] == "2.0.0"


def test_items_support_bounded_pagination_and_typed_output() -> None:
    response = client.get("/api/v1/items/?offset=1&limit=1")
    payload = response.json()
    assert response.status_code == 200
    assert payload["total"] == 3
    assert payload["offset"] == 1
    assert payload["limit"] == 1
    assert payload["data"] == [{"id": 2, "name": "Sample Item 2", "value": 200}]
    datetime.fromisoformat(payload["timestamp"])


def test_missing_item_is_a_stable_not_found() -> None:
    response = client.get("/api/v1/items/99")
    assert response.status_code == 404
    assert response.json() == {"detail": "Item not found"}


def test_openapi_describes_the_public_contract() -> None:
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert response.json()["info"]["version"] == "2.0.0"
    assert "/api/v1/items/" in response.json()["paths"]
