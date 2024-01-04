

from typing import List
from pydantic import BaseModel
from app.schemas.blog import CreateBlog
from app.schemas.user import UserBase


class ShowBlog(CreateBlog):
    id: int
    creator: UserBase

class ShowUser(BaseModel):
    id: int
    name:str
    email:str
    blogs: List[CreateBlog] = []