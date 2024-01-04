from fastapi import FastAPI
from app.routers import blogs, users

app = FastAPI()


# Dependency
app.include_router(users.router)
app.include_router(blogs.router)


# Users
