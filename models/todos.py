from pydantic import BaseModel

class Todo(BaseModel):
    nombre: str
    autor: str
    editorial: str
    edicion: float
    categoria: str
    precio: float