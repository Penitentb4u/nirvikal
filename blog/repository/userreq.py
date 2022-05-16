from sqlalchemy.orm import Session
from sqlalchemy import select
from blog import models,schemas
from fastapi import HTTPException,status

def checkattend(name:str,db:Session):
    #new_blog=models.Atten(date_time=date)
    crack=db.query(models.Atten).filter( models.Atten.name== name).all()
    return crack