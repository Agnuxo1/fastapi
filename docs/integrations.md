# Deployment integrations

This repository intentionally provides portable configuration contracts rather than
claiming live deployments or upstream adoption. Each target below uses the same
`app.main:app` ASGI entry point and the health endpoint `/api/v1/healthz`.

| Target | Contract | Local verification |
| --- | --- | --- |
| Vercel | `vercel.json` | JSON parse and entry-point check |
| Docker | `Dockerfile` | `docker build` when Docker is available |
| Docker Compose | `docker-compose.yml` | Compose schema review |
| Render | `render.yaml` | Required command and health path review |
| Railway | `railway.json` | JSON parse and health path check |
| Fly.io | `fly.toml` | Port and health path review |
| Google Cloud Run | `deploy/cloud-run.yaml` | Required service/image/probe fields |
| Kubernetes | `deploy/kubernetes.yaml` | Deployment/service/probe field checks |
| systemd | `deploy/fastapi-starter.service` | Unit command and hardening review |
| GitHub Actions | `.github/workflows/ci.yml` | CI file is exercised by pull requests |

No deployment command is run automatically, no cloud account is contacted, and no
credentials are required by the test suite. Build the local image as
`fastapi-deployment-starter:2.0.0`, then publish that exact image to the registry
required by a target before applying a registry-backed deployment.
