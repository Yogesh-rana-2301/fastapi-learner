from fastapi import APIRouter, Depends ,status, HTTPException,Response
from .. import schema, models, database
from sqlalchemy.orm import Session
from typing import List


router = APIRouter()


@router.post("/blog",status_code=201,tags=['BLOG']) # for the metadata       
async def create_blog(blog:schema.Blog, db: Session=Depends(database.get_db)): 

    new_blog=models.Blog(title=blog.title, body=blog.body, user_id=blog.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog

@router.get("/blog",response_model=List[schema.ShowBlog],tags=['BLOG'])
async def get_blogs(db: Session=Depends(database.get_db)):  
    blogs=db.query(models.Blog).all()
    return blogs



@router.get("/blog/{id}",response_model=schema.ShowBlog,tags=['BLOG'])  
async def get_blog(id,response:Response,db: Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first() 
    if not blog: 
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':f"{id} not found"}
    return blog



@router.put("/blog/{id}",status_code=status.HTTP_202_ACCEPTED,tags=['BLOG'])
async def update(id, request:schema.Blog, db: Session=Depends(database.get_db)):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'cant find')
    else:
        blog.update(request.model_dump())
        db.commit()
        return 'updated'




@router.delete('/blog/{id}',status_code=status.HTTP_404_NOT_FOUND,tags=['BLOG'])
async def destroy (id,db: Session=Depends(database.get_db)):
    db.query(models.Blog).filter(models.Blog.id==id).delete(
    synchronize_session="evaluate")
    db.commit()
    return 'done'

