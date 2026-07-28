from pydantic import BaseModel

class Blog(BaseModel):
    title: str
    body: str   
    

class ShowBlog(BaseModel):
    title: str
    body: str
    
    class Config():
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str

class User(BaseModel):
    name: str
    email: str
    password: str


class ShowUser(BaseModel):
    name: str
    email: str
    
    class Config():
        from_attributes = True