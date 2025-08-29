from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import Response, status, HTTPException

def get_all(db:Session):
    blogs=db.query(models.Blog).all()
    return blogs

def create (blog:schema.Blog,db:Session):
    new_blog=models.Blog(title=blog.title, body=blog.body, user_id=blog.user_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def get_one(id:int,response:Response,db:Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id).first() 
    if not blog: 
        response.status_code=status.HTTP_404_NOT_FOUND
        return {'detail':f"{id} not found"}
    return blog


def put_one(id:int,request:schema.Blog, db: Session):
    blog=db.query(models.Blog).filter(models.Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'cant find')
    else:
        blog.update(request.model_dump())
        db.commit()
        return 'updated'
    
def destroy_one(id:int,db:Session):
    db.query(models.Blog).filter(models.Blog.id==id).delete(
    synchronize_session="evaluate")
    db.commit()
    return 'done'