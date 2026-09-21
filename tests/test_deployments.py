import json
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_json_deployment_contracts_are_valid() -> None:
    for path in (ROOT / "vercel.json", ROOT / "railway.json"):
        payload = json.loads(path.read_text(encoding="utf-8"))
        assert isinstance(payload, dict)


def test_deployment_contracts_share_the_same_health_surface() -> None:
    expected = "/api/v1/healthz"
    for relative in ("render.yaml", "fly.toml", "deploy/cloud-run.yaml", "deploy/kubernetes.yaml"):
        assert expected in (ROOT / relative).read_text(encoding="utf-8")


def test_container_contract_is_non_root_and_exposes_asgi_entrypoint() -> None:
    dockerfile = (ROOT / "Dockerfile").read_text(encoding="utf-8")
    assert "USER appuser" in dockerfile
    assert "uvicorn app.main:app" in dockerfile
