# FastAPI Deployment Starter

A small, typed, testable FastAPI application that can be run locally or carried
between common deployment targets without changing the ASGI entry point. The
maintained application is `app.main:app` and the public API is deliberately
sample-only: it has no database, authentication, secret handling, or external
service calls.

## Features

- FastAPI application metadata and OpenAPI documentation at `/docs`.
- Typed item responses with bounded `offset`/`limit` pagination.
- Dependency-light liveness and readiness probes at `/api/v1/healthz` and
  `/api/v1/readyz`.
- Optional comma-separated CORS configuration via `FASTAPI_CORS_ORIGINS`.
- Real API tests, compile checks, and a deterministic local benchmark.
- Portable contracts for Vercel, Docker, Compose, Render, Railway, Fly.io,
  Google Cloud Run, Kubernetes, systemd, and GitHub Actions. These are tested
  configuration contracts, not claims of live deployments or upstream adoption.

## Local development

Python 3.12 or 3.13 is supported.

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# Unix: source .venv/bin/activate
python -m pip install -e ".[test]"
python -m pytest
python -m compileall -q app scripts tests
python -m scripts.benchmark
uvicorn app.main:app --reload --port 8000
```

Then open <http://127.0.0.1:8000/docs>.

## API surface

| Method | Path | Purpose |
| --- | --- | --- |
| GET | `/` | Accessible HTML landing page |
| GET | `/api/v1/healthz` | Liveness status |
| GET | `/api/v1/readyz` | Readiness status |
| GET | `/api/v1/items/` | Bounded sample collection |
| GET | `/api/v1/items/{item_id}` | One sample item, or 404 |
| GET | `/docs` | Swagger UI |
| GET | `/redoc` | ReDoc |

## Deployment

The root `Dockerfile`, `docker-compose.yml`, `vercel.json`, `render.yaml`,
`railway.json`, and `fly.toml` cover common platforms. Additional Cloud Run,
Kubernetes, and systemd contracts live under `deploy/`. See
[`docs/integrations.md`](docs/integrations.md) for the exact boundaries and
local verification performed. No deployment is run by the test suite and no
cloud credentials are required.

## Version history and license

The complete original 0.1.0 tree is preserved under
[`versions/0.1.0/`](versions/0.1.0/) with a source archive, manifest, and
SHA-256 evidence. The original repository did not include a license file; this
maintenance release does not infer a license for the original material. Review
and add the intended project license before redistribution.

## Security

Read [`SECURITY.md`](SECURITY.md). Do not put real credentials in issues,
fixtures, screenshots, or test output.
