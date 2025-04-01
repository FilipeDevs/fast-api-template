from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import schemas
from model import user
from db.database import get_db
from routes.auth import oauth2_scheme
from util import auth
from service.user_service import (
    register_user as register_user_service,
    get_user_by_username,
)

router = APIRouter()


@router.post("/register", response_model=schemas.User)
def register_user(user_data: schemas.UserCreate, db: Session = Depends(get_db)):
    return register_user_service(user_data, db)


async def get_current_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    username = auth.verify_token(token)
    if username is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return get_user_by_username(username, db)


@router.get("/users/me", response_model=schemas.User)
async def read_users_me(current_user: user.User = Depends(get_current_user)):
    return current_user
