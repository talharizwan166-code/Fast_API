from .. import schemas, database, models
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, HTTPException
from ..hashing import Hash
router = APIRouter(
    tags=['Authentication']
)

@router.post('/login')
def login(request: schemas.Login, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid credentials")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect password")
    return {"message": "Login successful"}