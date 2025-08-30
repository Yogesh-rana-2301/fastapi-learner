from datetime import datetime, timedelta, timezone
from fastapi import FastAPI,APIRouter, Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Annotated
from .. import schema,database,models,hashing,token
from sqlalchemy.orm import Session


router=APIRouter(
    tags=["LOGIN"]
)

@router.post('/login')

async def login(request: Annotated[OAuth2PasswordRequestForm, Depends()], db: Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.name==request.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user not found')
    if not hashing.Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credentials')
    else : 
        access_token = token.create_access_token(data={"sub": user.email})
        return {"access_token":access_token, "token_type":"bearer"}
    