from sqlalchemy.orm import Session
from . import models, schemas
from uuid import UUID
import logging

from fastapi import HTTPException

logger = logging.getLogger('uvicorn.error')
logger.setLevel(logging.DEBUG)

def create_url_information(db: Session, url_information: schemas.UrlInformation):
    logger.debug("Create URL Information")
    db_url_information = models.UrlInformation(None, url_information.url)
    db.add(db_url_information)
    db.commit()
    db.refresh(db_url_information)
    return db_url_information
    
def get_all_url_information(db: Session):
    logger.debug("Getting all URL information")
    DATA = db.query(models.UrlInformation).all()
    return DATA
    
def get_url_by_uuid(db: Session, url_uuid: str):
    logger.debug("Getting URL by UUID")
    data = db.query(models.UrlInformation).filter(models.UrlInformation.id == url_uuid).first()   
    return data
    
def create_url_with_alias(db: Session, url_information: schemas.UrlInformation):
    logger.debug(f"Creating URL Information with Alias: {url_information.id}")        
    
    if url_information.id > 20:
        raise HTTPException(status_code=402, detail="This Alias is too large please use something shorter")
    
    check_existence = db.query(models.UrlInformation).filter(models.UrlInformation.id == url_information.id).first()
    
    if check_existence:
        raise HTTPException(status_code=403, detail="This Alias already exists please try another!")
        
    db_url_with_alias = models.UrlInformation(url_information.id, url_information.url)
    db.add(db_url_with_alias)
    db.commit()
    db.refresh(db_url_with_alias)
    return db_url_with_alias
    