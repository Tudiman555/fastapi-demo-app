from typing import List
from fastapi import Depends, FastAPI, HTTPException, status
from app.auth import get_password_hash
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.blog import CreateBlog, UpdateBlog
from app.models import Blog, User
from app.schemas.user import CreateUser
from app.schemas.user_blog import ShowBlog, ShowUser

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def index():
    return "hi"


@app.get("/blog", response_model=List[ShowBlog], tags=["blogs"])
def all(limit=10, db: Session = Depends(get_db)):
    return db.query(Blog).limit(limit).all()


@app.post("/blog", status_code=status.HTTP_201_CREATED, tags=["blogs"], response_model=ShowBlog)
def create(blog: CreateBlog, db: Session = Depends(get_db)):
    new_blog = Blog(title=blog.title, body=blog.body, creator_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/blog/{id}", response_model=ShowBlog, tags=["blogs"])
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!"
        )
    return blog


@app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["blogs"])
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id)
    if not blog.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!"
        )
    blog.delete(synchronize_session=False)
    db.commit()
    return "Done"


@app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=["blogs"])
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


# Users


@app.post("/user", response_model=ShowUser, tags=["users"])
def create_user(request_body: CreateUser, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == request_body.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already exists!"
        )
    user_data = request_body.model_dump()
    # Override the password field
    user_data["password"] = get_password_hash(request_body.password)

    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user
