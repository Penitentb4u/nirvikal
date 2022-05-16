from tokenize import String
from blog.oauth2 import get_current_user
from fastapi import APIRouter,Depends,status,HTTPException
from blog import schemas,database,models,oauth2
from typing import List
from sqlalchemy.orm import Session
from blog.repository import userreq

router=APIRouter( 
    prefix="/userreq",
    tags=['Userreq'])
get_db=database.get_db

@router.get('/{str}',status_code=200,response_model=List[schemas.ShowUserAttend] )
def show(name:str, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return userreq.checkattend(name,db)