from fastapi import APIRouter, FastAPI

from src.api.endpoints.healthcheck import healthcheck_router


def init_routers(app: FastAPI) -> None:
    root_router = APIRouter()

    root_router.include_router(healthcheck_router)
    app.include_router(root_router)
    print('test')
