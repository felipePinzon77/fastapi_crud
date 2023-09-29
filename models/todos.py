from pydantic import BaseModel

class Todo(BaseModel):
    nombre: str
    numero: int