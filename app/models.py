from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True)
    title = Column(String,index=True)
    body = Column(Text)
    published = Column(Boolean, default=False)
    creator_id = Column(Integer, ForeignKey("users.id"),nullable=False)
    creator = relationship('User',back_populates='blogs')

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String,index=True,unique=True,nullable=False)
    password = Column(String,nullable=False)
    blogs = relationship('Blog',back_populates='creator')

