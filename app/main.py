from fastapi import Depends, FastAPI, HTTPException, status
from app.database import SessionLocal
from sqlalchemy.orm import Session
from app.schemas.blog import CreateBlog
from app.models import Blog 

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

@app.get("/blog")
def all(limit=10, db: Session = Depends(get_db)):
    return db.query(Blog).limit(limit).all()


@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create(blog: CreateBlog, db: Session = Depends(get_db)):
    new_blog = Blog(title=blog.title, body=blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return {"data": new_blog}


@app.get("/blog/{id}")
def show(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if  not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!") 
    return blog

@app.delete("/blog/{id}" ,status_code=status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).delete(synchronize_session=False)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!") 
    db.commit()
    return 'Done'

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED)
# def update(id: int, blog: UpdateBlog, db: Session = Depends(get_db)):
#     updated_blog = db.query(Blog).filter(Blog.id == id).update({**blog.__dict__})
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found !!") 
#     db.commit()
#     return 'Done'


