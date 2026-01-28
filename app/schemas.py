from pydantic import BaseModel


class HealthResponse(BaseModel):
    status: str


class ErrorResponse(BaseModel):
    error: str
    message: str
    details: dict | None = None
