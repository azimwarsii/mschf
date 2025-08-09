from fastapi import APIRouter
from ..schemas import StatusResponse

router = APIRouter()

@router.get("/auth/status", response_model=StatusResponse)
def auth_status():
    return StatusResponse(status="ready", message="Authentication system ready")

