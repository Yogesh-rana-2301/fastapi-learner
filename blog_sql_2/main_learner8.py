
from fastapi import FastAPI, Depends ,status, HTTPException,Response
from typing import Optional

import uvicorn   
from . import schema
from . import models 
from .database import engine, SessionLocal
from sqlalchemy.orm import Session


app=FastAPI()

models.base.metadata.create_all (bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield(db)   
    finally:
        db.close()


#visit https://docs.python.org/3/library/http.html
@app.post ("/blog",status_code=201)       #pass the parameter of status_code along with it to get the correct session_code

#or throught the documentation. do ->
# @app.post ("/blog",status_code=status.HTTP_201_CREATED)


async def create_blog(blog:schema.Blog, db: Session=Depends(get_db)): 

    new_blog=models.User(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
async def get_blogs(db: Session=Depends(get_db)):  
    blogs=db.query(models.User).all()
    return blogs



@app.get("/blog/{id}")
async def get_blog(id,response:Response,db: Session=Depends(get_db)):
    blog=db.query(models.User).filter(models.User.id==id).first() 
    if not blog: 
        #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
        #or
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':f"{id} not found"}
    return blog
