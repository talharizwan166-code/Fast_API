from typing import List
from fastapi import APIRouter,Depends,status
from .. import schemas, database, models
from sqlalchemy.orm import Session

get_db = database.get_db

router = APIRouter()


@router.get('/blog', status_code=200,response_model=list[schemas.ShowBlog],tags=['blogs'])
def all(db : Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post('/blog', status_code=status.HTTP_201_CREATED,tags=['Blogs']) 
def create(request: schemas.Blog, db : Session=Depends(get_db)):

    new_blog = models.Blog(title=request.title, body=request.body,user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog