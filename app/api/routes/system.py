from fastapi import APIRouter

from app.api.schemas import ServiceStatus
from app.core.config import settings

router = APIRouter(tags=["system"])


@router.get("/healthz", response_model=ServiceStatus, summary="Liveness probe")
def health() -> ServiceStatus:
    return ServiceStatus(
        status="ok",
        service=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
    )


@router.get("/readyz", response_model=ServiceStatus, summary="Readiness probe")
def readiness() -> ServiceStatus:
    return ServiceStatus(
        status="ready",
        service=settings.PROJECT_NAME,
        version=settings.VERSION,
        environment=settings.ENVIRONMENT,
    )
