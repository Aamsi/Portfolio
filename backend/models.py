from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel

Base = declarative_base()

class User(BaseModel):
    first_name: str
    last_name: str = None
    age: int

    class Config:
        orm_mode = True