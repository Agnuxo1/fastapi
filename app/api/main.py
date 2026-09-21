from fastapi import APIRouter

from app.api.routes import items
from app.api.routes import system

api_router = APIRouter()
api_router.include_router(system.router)
api_router.include_router(items.router)
