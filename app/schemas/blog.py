from typing import Optional
from pydantic import BaseModel

class CreateBlog(BaseModel):
    title: str
    body: str
    published: bool

# class UpdateBlog(BaseModel): 
#     title: Optional[str]
#     body: Optional[str]
#     published: Optional[bool]