from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from . import models, schemas, auth
from .database import get_db
from datetime import timedelta

router = APIRouter()

@router.post("/signup", response_model=schemas.UserResponse)
async def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # Check if user exists
    if user.user_type == "student":
        existing_user = db.query(models.StudentLogin).filter(
            (models.StudentLogin.email == user.email) | 
            (models.StudentLogin.username == user.username)
        ).first()
        model = models.StudentLogin
    else:
        existing_user = db.query(models.TeacherLogin).filter(
            (models.TeacherLogin.email == user.email) | 
            (models.TeacherLogin.username == user.username)
        ).first()
        model = models.TeacherLogin

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already registered"
        )

    # Create new user
    hashed_password = auth.get_password_hash(user.password)
    db_user = model(
        username=user.username,
        email=user.email,
        password=hashed_password
    )
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user 