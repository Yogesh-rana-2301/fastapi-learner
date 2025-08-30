from fastapi import FastAPI
from .database import engine, SessionLocal
from sqlalchemy.orm import Session
from . import schema,models
from .routers import user,blog,authentication


app=FastAPI()

models.base.metadata.create_all (bind=engine)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)




