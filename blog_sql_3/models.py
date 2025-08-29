from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from .database import base
from sqlalchemy.orm import relationship

class Blog(base):
    __tablename__= "blogs"
    id = Column (Integer, primary_key=True,index=True)
    title = Column (String)
    body = Column (String)    
    user_id=Column(Integer, ForeignKey('user.id'))  #table name

    creator=relationship("User",back_populates="blogs")

class User(base): 
    __tablename__="user"
    id = Column (Integer, primary_key=True,index=True)
    name = Column (String) 
    email = Column (String)    
    password=Column(String)

    blogs=relationship("Blog",back_populates="creator")
   