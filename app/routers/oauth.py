from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..dependencies import get_db
from ..schemas import OAuthStatus, OAuthLogin, AuthResponse
from ..services import OAuthService

router = APIRouter()
oauth_service = OAuthService()

@router.get("/auth/oauth/status", response_model=OAuthStatus)
def oauth_status():
    return OAuthStatus(status="ready")

@router.post("/auth/oauth", response_model=AuthResponse)
async def oauth_login(oauth_data: OAuthLogin, db: Session = Depends(get_db)):
    try:
        return oauth_service.process_oauth_login(db, oauth_data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/auth/oauth/accounts/{user_id}")
def get_user_oauth_accounts(user_id: int, db: Session = Depends(get_db)):
    accounts = oauth_service.get_user_oauth_accounts(db, user_id)
    return {"accounts": accounts}

@router.delete("/auth/oauth/disconnect/{user_id}/{provider}")
def disconnect_oauth_account(user_id: int, provider: str, db: Session = Depends(get_db)):
    success = oauth_service.disconnect_oauth_account(db, user_id, provider)
    if not success:
        raise HTTPException(status_code=404, detail="OAuth account not found")
    return {"message": f"Disconnected {provider} account"}
