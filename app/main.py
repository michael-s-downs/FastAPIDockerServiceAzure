from fastapi import FastAPI
from pydantic import BaseModel


class Query(BaseModel):
    text: str
    role: str


app = FastAPI()


@app.get("/")
async def read_item():
    return {"message": "Welcome to our app"}


@app.get("/hello/{name}")
async def read_item(name):
    return {"message": f"Hello {name}, how are you?"}


@app.post("/query/")
async def create_query(query: Query):
    return {"message": f"You asked: {query.text} to be answered using role: {query.role}"}