from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import base

class Blog(base):
    __tablename__= "blogs"
    id = Column (Integer, primary_key=True,index=True)
    title = Column (String)
    body = Column (String)    


class User(base): 
    __tablename__="user"
    id = Column (Integer, primary_key=True,index=True)
    name = Column (String)
    email = Column (String)    
    password=Column(String)