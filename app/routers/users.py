
from fastapi import status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from .. import models, schemas, utils

router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/", status_code=status.HTTP_201_CREATED,  response_model=schemas.UserResponse)
def create_user(userData : schemas.UserCreate ,db: Session = Depends(get_db)):
    
    hashed_password = utils.hash(userData.password)
    userData.password = hashed_password

    user = models.User(**userData.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"user with id {id} was not found.")

    return user