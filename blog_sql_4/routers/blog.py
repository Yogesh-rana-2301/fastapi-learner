from fastapi import APIRouter, Depends ,status, HTTPException,Response
from .. import schema, models, database, oauth2
from sqlalchemy.orm import Session
from typing import List
from ..repo import blog,user
from typing import Annotated


router = APIRouter(
    prefix="/blog",
    tags=['BLOG']
)


@router.post("/",status_code=201) # for the metadata       
async def create_blog(blog:schema.Blog, db: Session=Depends(database.get_db),current_user: schema.User=Depends(oauth2.get_current_user)): 
    return blog.create(blog,db)

@router.get("/",response_model=List[schema.ShowBlog])
async def get_blogs(db: Session=Depends(database.get_db), current_user: schema.User=Depends(oauth2.get_current_user)):  
    return blog.get_all(db)



@router.get("/{id}",response_model=schema.ShowBlog)  
async def get_blog(id,db: Session=Depends(database.get_db),current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.get_one(id,db)



@router.put("/{id}",status_code=status.HTTP_202_ACCEPTED)
async def update(id, request:schema.Blog, db: Session=Depends(database.get_db),current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.put_one(id,request,db)


@router.delete('/{id}',status_code=status.HTTP_404_NOT_FOUND)
async def destroy (id,db: Session=Depends(database.get_db),current_user: schema.User=Depends(oauth2.get_current_user)):
    return blog.destroy_one(id,db)

