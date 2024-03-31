from typing import Optional
from xmlrpc.client import boolean
from fastapi import FastAPI
from sqlmodel import Field , SQLModel , create_engine

class Todos(SQLModel , Table=True):
    id: Optional[int] = Field(default=None , primary_key=True)
    content: str
    is_done: bool= Field(default=False)

db_url = "postgresql://neondb_owner:lWY64ucFjTdx@ep-shy-butterfly-a5s17rvv.us-east-2.aws.neon.tech/practice-todos?sslmode=require"    
engine = create_engine(db_url , echo=True)   
SQLModel.metadata.create_all(engine) 
app = FastAPI(
    title="Practice Todo",
)
@app.get("/")
def read_root():
    return {"Hello": "World"}