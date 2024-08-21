from sqlalchemy import Column, String, Integer
from uuid import uuid4, UUID
from sqlalchemy.orm import mapped_column, Mapped
import zlib
import hashlib

from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String)
    password = Column(String)
    
    
    def __init__(self, username, password):
        
        self.username = username
        self.password = password

class UrlInformation(Base):
    __tablename__ = "url_information"
    
    id = Column(String, primary_key=True)
    url = Column(String)
    
    def __init__(self, id, url):
        
        if id == None:
            crc32_hash = hex(zlib.crc32(str(uuid4()).encode("utf-8")))
            self.id = crc32_hash
        else:   
            self.id = id
        self.url = url