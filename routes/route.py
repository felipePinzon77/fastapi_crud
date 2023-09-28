from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_book
from schema.schemas import list_serial
from bson import ObjectId
from config.database import collection_sell
from fastapi import HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

router = APIRouter()


# GET
@router.get("/")
async def get_todos():
    todos = list_serial(collection_book.find())
    return todos


# POST
@router.post("/")
async def post_todo(todo: Todo):
    collection_book.insert_one(dict(todo))


# PUT
@router.put("/{id}")
async def put_todo(id: str, todo: Todo):
    todo_actualizado = collection_book.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    if todo_actualizado is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No existe esta tarea")
    
# Si la tarea se ha vendido, la movemos a la colección "vendidos"
    if todo.vendido:
        collection_sell.insert_one(dict(todo))
    collection_book.delete_one({"_id": todo_actualizado["_id"]})
    return JSONResponse(jsonable_encoder(todo_actualizado))

# DELETE
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_book.find_one_and_delete({"_id": ObjectId(id)})


# VENTA
