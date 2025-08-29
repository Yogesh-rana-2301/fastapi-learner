from fastapi import APIRouter, Depends ,status, HTTPException,Response
from .. import schema, models, database
from sqlalchemy.orm import Session
from typing import List
from .. import hashing


router = APIRouter()


@router.post('/user',response_model=schema.ShowUser,tags=['USER'])
async def create_user(request:schema.User, db: Session=Depends(database.get_db)):
    hashed_pass=hashing.Hash.bcrypt(request.password)
    new_user=models.User(name=request.name, email=request.email,password=hashed_pass)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/user/{id}',response_model=schema.ShowUser,tags=['USER'])
async def get_user(id:int,db: Session=Depends(database.get_db) ):
    user=db.query(models.User).filter(models.User.id==id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'cant find')
    return user.first()

    