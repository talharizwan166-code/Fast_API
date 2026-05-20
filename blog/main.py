from fastapi import FastAPI
from  . import schemas
app=FastAPI()



@app.post('/blog')
def create(requst:schemas.blog):
    return requst 