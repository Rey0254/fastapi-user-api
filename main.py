from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = []  # Lista para almacenar usuarios temporalmente

class User(BaseModel):
    name: str
    age: int
    email: str

@app.post("/user")
async def create_user(user: User):
    users.append(user)
    return {"message": "Usuario guardado correctamente", "user": user}
