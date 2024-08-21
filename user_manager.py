from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID, uuid4
import logging
import hashlib

from fastapi import HTTPException

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)


def password_hasher(password: str):
    return hashlib.sha256(password.encode("utf-8")).hexdigest()


def create_user(db: Session, user: schemas.UserCreate):
    logger.debug("Creating User Account")
    
    db_user = models.User(user.username, password_hasher(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    
    
def get_user_by_id(db: Session, user_id: int):
    logger.debug(f"Getting User by ID: {user_id}" )
    data = db.query(models.User).filter(models.User.id == user_id).first()   
    return data