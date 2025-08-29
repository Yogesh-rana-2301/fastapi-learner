from sqlalchemy.orm import Session
from .. import models, schema
from fastapi import Response, status, HTTPException
from .. import hashing


def create_user(request,db:Session):
    hashed_pass=hashing.Hash.bcrypt(request.password)
    new_user=models.User(name=request.name, email=request.email,password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_user(id:int,db:Session):
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'cant find')
    return user.first()