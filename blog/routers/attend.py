from tokenize import String
from blog.oauth2 import get_current_user
from fastapi import APIRouter,Depends,status,HTTPException
from blog import schemas,database,models,oauth2
from typing import List
from sqlalchemy.orm import Session
from blog.repository import attend

router=APIRouter(
    prefix="/attend",
    tags=['Attendance'])

get_db=database.get_db

@router.post('/',status_code=status.HTTP_201_CREATED)
def create(request:schemas.Attendance,db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return attend.create(request,db) 

@router.get('/',response_model=List[schemas.ShowAttend] )
def all(db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return attend.get_all(db)

@router.get('/{str}',status_code=200,response_model=List[schemas.ShowDate] )
def show(date:str, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return attend.checkdate(date,db)

@router.get('/{str}',status_code=200,response_model=List[schemas.ShowUserAttend] )
def show(name:str, db:Session=Depends(get_db),current_user:schemas.User=Depends(oauth2.get_current_user)):
    return attend.checkattend(name,db)