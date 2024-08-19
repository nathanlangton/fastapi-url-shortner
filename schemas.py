from pydantic import BaseModel
from uuid import UUID

class UrlInformationBase(BaseModel):
    url: str
    
class UrlInformationCreate(UrlInformationBase):
    pass

class UrlInformation(UrlInformationBase):
    id: str
    
    class Config:
        orm_mode = True
    