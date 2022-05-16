from fastapi import FastAPI
from blog import schemas,models
from blog.database import engine
from blog.routers import blog,user,authentication,attend,userreq



app= FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(attend.router)
app.include_router(userreq.router)