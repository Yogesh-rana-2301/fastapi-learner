# everything related to users now 


from fastapi import FastAPI, Depends ,status, HTTPException,Response
from typing import Optional

import uvicorn   
from . import schema
from . import models 
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

from passlib.context import CryptContext

from typing import List
from . import hashing


app=FastAPI()

models.base.metadata.create_all (bind=engine) #whatever in the model creating int the tablePlus or wherever

def get_db():
    db=SessionLocal()
    try:
        yield(db)   
    finally:
        db.close()


@app.post ("/blog",status_code=201,tags=['BLOG']) # for the metadata       
async def create_blog(blog:schema.Blog, db: Session=Depends(get_db)): 

    new_blog=models.Blog(title=blog.title, body=blog.body, user_id=blog.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

@app.get("/blog",response_model=List[schema.ShowBlog],tags=['BLOG'])
async def get_blogs(db: Session=Depends(get_db)):  
    blogs=db.query(models.Blog).all()
    return blogs



@app.get("/blog/{id}",response_model=schema.ShowBlog,tags=['BLOG'])  
async def get_blog(id,response:Response,db: Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first() 
    if not blog: 
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':f"{id} not found"}
    return blog



@app.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED,tags=['BLOG'])
async def update(id, request:schema.Blog, db: Session=Depends(get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'cant find')
    else:
        blog.update(request.model_dump())
        db.commit()
        return 'updated'




@app.delete('/blog/{id}',status_code=status.HTTP_404_NOT_FOUND,tags=['BLOG'])
async def destroy (id,db: Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(
    synchronize_session="evaluate")
    db.commit()
    return 'done'




@app.post('/user',response_model=schema.ShowUser,tags=['USER'])
async def create_user(request:schema.User, db: Session=Depends(get_db)):
    hashed_pass=hashing.Hash.bcrypt(request.password)
    new_user=models.User(name=request.name, email=request.email,password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get('/user/{id}',response_model=schema.ShowUser,tags=['USER'])
async def get_user(id:int,response:Response,db: Session=Depends(get_db) ):
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'cant find')
    return user.first()

    