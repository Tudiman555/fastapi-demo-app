from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Blog
from app.schemas.blog import CreateBlog, UpdateBlog
from app.schemas.user_blog import ShowBlog

router = APIRouter(prefix="/blog", tags=["Blogs"])


@router.get("", response_model=List[ShowBlog])
def all(limit=10, db: Session = Depends(get_db)):
    return db.query(Blog).limit(limit).all()


@router.post("", status_code=status.HTTP_201_CREATED, response_model=ShowBlog)
def create(blog: CreateBlog, db: Session = Depends(get_db)):
    new_blog = Blog(title=blog.title, body=blog.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@router.get("/{id}", response_model=ShowBlog)
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!"
        )
    return blog


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request_body: UpdateBlog, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!"
        )
    blog.update(
        {**request_body.model_dump(exclude_unset=True)}
    )  # exclude_unset=True removes all those field which are null
    db.commit()
    return "Done"
