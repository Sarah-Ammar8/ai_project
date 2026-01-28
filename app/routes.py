from fastapi import APIRouter
from .services import get_health_status
from .schemas import HealthResponse

router = APIRouter()

@router.get("/")
def root():
    return {"service": "base-backend", "docs": "/docs"}

@router.get("/health", response_model=HealthResponse)
def health_check():
    return HealthResponse(status=get_health_status())
