
from fastapi import FastAPI,APIRouter, Depends,HTTPException,status
from .. import schema,database,models,hashing
from sqlalchemy.orm import Session

router=APIRouter(
    tags=["LOGIN"]
)

@router.post('/login')

async def login(request: schema.login, db: Session=Depends(database.get_db)):
    user=db.query(models.User).filter(models.User.name==request.username).first()
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'user not found')
    if not hashing.Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'invalid credentials')
    else : 
        return user