from fastapi import APIRouter, HTTPException
from typing import List
from models.todo import Todo, TodoCreate, TodoUpdate
from datetime import datetime

router = APIRouter()

# In-memory storage for todos
todos = []
todo_id_counter = 1

@router.get("/", response_model=List[Todo])
async def get_todos():
    return todos

@router.post("/", response_model=Todo)
async def create_todo(todo: TodoCreate):
    global todo_id_counter
    new_todo = Todo(
        id=todo_id_counter,
        title=todo.title,
        description=todo.description,
        created_at=datetime.now()
    )
    todos.append(new_todo)
    todo_id_counter += 1
    return new_todo

@router.get("/{todo_id}", response_model=Todo)
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.put("/{todo_id}", response_model=Todo)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    for todo in todos:
        if todo.id == todo_id:
            if todo_update.title is not None:
                todo.title = todo_update.title
            if todo_update.description is not None:
                todo.description = todo_update.description
            if todo_update.completed is not None:
                todo.completed = todo_update.completed
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found") 