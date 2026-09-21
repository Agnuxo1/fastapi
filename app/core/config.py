import os

from pydantic import BaseModel


class Settings(BaseModel):
    PROJECT_NAME: str = os.getenv("FASTAPI_PROJECT_NAME", "FastAPI Deployment Starter")
    VERSION: str = os.getenv("FASTAPI_VERSION", "2.0.0")
    API_V1_STR: str = os.getenv("FASTAPI_API_V1_STR", "/api/v1")
    ENVIRONMENT: str = os.getenv("FASTAPI_ENVIRONMENT", "development")
    CORS_ORIGINS: str = os.getenv("FASTAPI_CORS_ORIGINS", "")

    @property
    def cors_origins(self) -> list[str]:
        return [origin.strip() for origin in self.CORS_ORIGINS.split(",") if origin.strip()]


settings = Settings()
