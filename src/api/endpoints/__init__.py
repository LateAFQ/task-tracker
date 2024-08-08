from fastapi import APIRouter


from src.api.endpoints.healthcheck import healthcheck_router

root_router = APIRouter()

root_router.include_router(healthcheck_router)
