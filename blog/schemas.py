from pydantic import BaseModel

class blog(BaseModel):
    tittle: str
    body: str