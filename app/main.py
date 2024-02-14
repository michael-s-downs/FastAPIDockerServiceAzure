from fastapi import FastAPI
from pydantic import BaseModel

class Query(BaseModel):
    text: str
    role: str

app = FastAPI()

@app.get("/")
async def top_level():
    return {"message": "Welcome to the Outlet Query Tool Gen-AI-over-API Service.  You are at the top. For all available APIs see /docs"}

@app.get("/hello/{name}")
async def read_item(name):
    return {"message": f"Hello {name}, how are you?"}

@app.post("/query/")
async def create_query(query: Query):
    return {"Mock Return": f"You asked: {query.text} to be answered using role: {query.role}.  This will be replaced with data return."}

@app.get("/refreshhelpdb/")
async def refresh_help_db():
    #do something...
    return {"message": f"You're request to refresh the local Chroma DB Vector Store has been successful"}

@app.get("/gethelpdbinfo/")
async def get_help_db_info():
    return {"Mock Return": f"This will be replaced with info about the Help DB"}