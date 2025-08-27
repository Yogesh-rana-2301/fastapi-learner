from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import base

class User(base):
    __tablename__= "users"
    id = Column (Integer, primary_key=True,index=True)
    title = Column (String)
    body = Column (String)    