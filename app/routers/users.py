from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.auth import get_password_hash
from app.database import get_db
from app.models import User
from app.schemas.user import CreateUser
from app.schemas.user_blog import ShowUser

router = APIRouter(prefix="/user", tags=["Users"])


@router.post("", response_model=ShowUser)
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
