from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_book
from schema.schemas import list_serial
from bson import ObjectId

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
    collection_book.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})


# DELETE
@router.delete("/{id}")
async def delete_todo(id: str):
    collection_book.find_one_and_delete({"_id": ObjectId(id)})