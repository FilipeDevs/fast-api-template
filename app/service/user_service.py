from sqlalchemy.orm import Session
from fastapi import HTTPException
from schemas import schemas
from model import user
from util import auth


def register_user(user_data: schemas.UserCreate, db: Session):
    db_user = (
        db.query(user.User).filter(user.User.username == user_data.username).first()
    )
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = auth.get_password_hash(user_data.password)
    new_user = user.User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user_by_username(username: str, db: Session):
    db_user = db.query(user.User).filter(user.User.username == username).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
