from typing import List
from pydantic import BaseModel


class UserBase(BaseModel):
    name: str
    email: str

class CreateUser(UserBase):
    password: str
