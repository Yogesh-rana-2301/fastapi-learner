from fastapi import APIRouter, Depends ,status, HTTPException,Response
from .. import schema, models, database
from sqlalchemy.orm import Session
from typing import List
from .. import hashing
from ..repo import blog,user

#refractoring
router = APIRouter(
    prefix="/user",
    tags=['USER']
)


@router.post('/',response_model=schema.ShowUser)
async def create_user(request:schema.User, db: Session=Depends(database.get_db)):
    return user.create_user(request,db)


@router.get('/{id}',response_model=schema.ShowUser)
async def get_user(id:int,db: Session=Depends(database.get_db) ):
    return user.get_user(id,db)

    