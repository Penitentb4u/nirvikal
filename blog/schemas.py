from turtle import title
from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
    title:str
    body:str
 
class Blog(BlogBase):
    class Config():
        orm_mode=True


class User(BaseModel):
    name:str
    email:str
    password:str
    roll:str
    
class ShowUser(BaseModel):
    name:str
    email:str
    password:str
    roll:str
    #blogs: List[Blog]=[]
    class Config():
        orm_mode=True

class ShowBlog(BaseModel):
    title:str
    body:str
    creator:ShowUser

    class Config():
        orm_mode=True    

class Login(BaseModel):
    username:str
    password:str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None

class Attendance(BaseModel):
    name:str
    roll:str
    status_now:bool
    #class Config():
    #    orm_mode=True    

class ShowAttend(BaseModel):
    name:str
    roll:str
    date_time:str
    status_now:bool
    #creator:ShowUser
    class Config():
        orm_mode=True    

class ShowUserAttend(BaseModel):
    name:str
    roll:str
    date_time:str
    status_now:bool
    class Config():
        orm_mode=True  

class ShowDate(BaseModel):
    name:str
    roll:str
    date_time:str
    status_now:bool
    class Config():
        orm_mode=True 
