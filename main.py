from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Numbers(BaseModel):
    a: int
    b: int
@app.get("/")
def home():
    return {"message": "MCP Server is live!"}

@app.post("/sum")
def calculate_sum(data: Numbers):
    result = data.a + data.b
    return {"result": result}

class Greeting(BaseModel):
    name: str

@app.post("/greet")
def greet_user(data: Greeting):
    return {"message": f"Hello, {data.name}!"}

