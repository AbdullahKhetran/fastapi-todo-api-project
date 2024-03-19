from fastapi import FastAPI
from dummy_data import todos
# interacting through service layer
from service import todo as service
from model.todo import Todo

app = FastAPI()


@app.get("/")
def get_todos() -> list[Todo]:
    return service.get_todos()


@app.post("/")
def create_todo(todo: Todo):
    return service.create_todo(todo)


@app.patch("/")
def modify_todo(todo_id: int, updated_todo: Todo):
    return service.modify_todo(todo_id, updated_todo)


@app.delete("/")
def delete_todo(todo_id: int):
    return service.delete_todo(todo_id)


# run `uvicorn main:app`
