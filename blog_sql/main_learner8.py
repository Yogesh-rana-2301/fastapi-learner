#https://www.sqlalchemy.org
#fastapi and sql 
#if this file was created inside other folder for example blog and is being tracked from here 
# then in the run command be uvicorn blog.main_learner8:app --reload
#i would be running with (uvicorn blog_sql.main_learner8:app --reload)
# the code is somewhat similar to the whole post code (but i would be storing the post queries in a database )
#

from fastapi import FastAPI, Depends
from typing import Optional
# from pydantic import BaseModel #wont be using this because sending this to the schema file here
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
        yield(db)  # yield is basically a return but dont terminates after excution 
    finally:
        db.close()

@app.post ("/blog")
async def create_blog(blog:schema.Blog, db: Session=Depends(get_db)):    #doing this becasue Session is not a pydatic thing, so usign inbuilt from fastapi

    new_blog=models.User(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

