# AGENTS.md — FastAPI Deployment Starter

## Contract

- Keep the application importable as `app.main:app`.
- Keep `/api/v1/healthz` and `/api/v1/readyz` dependency-light and machine-readable.
- Preserve typed response models and bounded pagination.
- Do not add credentials, real external services, telemetry, or claims of upstream adoption.
- Deployment files are portable examples and must be tested as local contracts; they are not proof of a live deployment.
- Preserve each previous release under `versions/<version>/` with a manifest and SHA-256 evidence.

## Verification

```bash
python -m pytest
python -m compileall -q app scripts tests
python -m scripts.benchmark
```
