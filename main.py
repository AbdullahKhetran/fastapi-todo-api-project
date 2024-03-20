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
def modify_todo(updated_todo: Todo):
    return service.modify_todo(updated_todo)


@app.delete("/delete/{id}")
def delete_todo(id: str):
    return service.delete_todo(id)


# run `uvicorn main:app --relaod`
