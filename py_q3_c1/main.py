from typing import Optional
from fastapi import FastAPI, HTTPException
from sqlmodel import Field , SQLModel , create_engine , Session , select
from pydantic import BaseModel , Field

class Todos(SQLModel , table=True):
    id: Optional[int] = Field(default=None , primary_key=True)
    content: str
    is_complete: bool= Field(default=False)


#databse url
db_url = "postgresql://neondb_owner:lWY64ucFjTdx@ep-shy-butterfly-a5s17rvv.us-east-2.aws.neon.tech/practice-todos?sslmode=require"    

#creating engine
engine = create_engine(db_url , echo=True)  

def create_table():
    SQLModel.metadata.create_all(engine) 

def insert_data_into_table(content: str):
    with Session(engine) as session:
        data: Todos = Todos(content=content)
        #session add
        session.add(data)  
        #session commit 
        session.commit() 


app = FastAPI(
    title="Practice Todo",
)

class User_Data(BaseModel):
    content: str = Field(nullable=False)
    is_complete: bool= False

@app.get("/")
def route_root():
    return {"Hello": "World"}

@app.post('/todos')
def add_todos_route(user_todos : User_Data):
    if user_todos.content.strip():
        insert_data_into_table(user_todos.content)
        return {"message": "Todos added successfully"}
    else:
        raise HTTPException(status_code=404 , detail="Todos not added")