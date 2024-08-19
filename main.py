import sentry_sdk
from sqlalchemy.orm import Session

from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from . import url_shortner
from .database import SessionLocal, engine
from . import models, schemas
from uuid import UUID

app = FastAPI(title="URL Shortner", debug=True)
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/health")
async def health_check():
    return {"message": "HEALTHY"}
    
@app.get("/get-all", response_model=list[schemas.UrlInformation])
async def get_all_url(db: Session = Depends(get_db)):
    return url_shortner.get_all_url_information(db)
   
@app.get("/{url_uuid}")
async def get_url_by_uuid(url_uuid: str, db: Session = Depends(get_db)):
    return url_shortner.get_url_by_uuid(db, url_uuid)
    
@app.post("/add-url", response_model=schemas.UrlInformation)
async def add_url(url_information: schemas.UrlInformationCreate, db: Session = Depends(get_db)):
    return url_shortner.create_url_information(db, url_information)

