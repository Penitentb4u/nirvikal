from genericpath import exists
from sqlalchemy.orm import Session
from sqlalchemy import select
from blog import models,schemas
from fastapi import HTTPException,status
import datetime

def get_all(db):
    blogs=db.query(models.Atten).all()
    return blogs

def create(request:schemas.Attendance ,db:Session):
    new_blog=models.Atten(name=request.name,roll=request.roll,user_id=1 ,date_time=datetime.date.today(),status_now=request.status_now)
    segs=db.query(models.Atten).where( models.Atten.name== new_blog.name,models.Atten.date_time==new_blog.date_time) 
    #if not segs.first():
    #sax=select(models.Atten).where(models.Atten.name.in_(["string4"])) #.where(models.Atten.date_time.in_(new_blog.date_time))"""
    #print(sax)
    if not segs.first():
        db.add(new_blog)
        db.commit()
        db.refresh(new_blog)
        return new_blog
    else:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT,detail=f"{new_blog.name} already exists on date {new_blog.date_time}")
    
def checkdate(date:str,db:Session):
    #new_blog=models.Atten(date_time=date)
    rack=db.query(models.Atten).filter( models.Atten.date_time== date).all()
    return rack

def checkattend(name:str,date:str,db:Session):
    #new_blog=models.Atten(date_time=date)
    crack=db.query(models.Atten).filter( models.Atten.name== name,models.Atten.date_time== date).all()
    return crack

