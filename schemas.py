from pydantic import BaseModel
from uuid import UUID

class UrlInformationBase(BaseModel):
    url: str
    
class UrlInformationCreate(UrlInformationBase):
    pass

class UrlInformation(UrlInformationBase):
    id: str
    
    
class UserBase(BaseModel):
    username: str
    password: str


class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    

    