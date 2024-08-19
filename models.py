from sqlalchemy import Column, String
from uuid import uuid4, UUID
from sqlalchemy.orm import mapped_column, Mapped
import zlib

from .database import Base

class UrlInformation(Base):
    __tablename__ = "url_information"
    
    id = Column(String, primary_key=True)
    url = Column(String)
    
    def __init__(self, url):
        
        crc32_hash = hex(zlib.crc32(str(uuid4()).encode("utf-8")))
        
        self.id = crc32_hash
        self.url = url