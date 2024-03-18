from fastapi import FastAPI
from dummy_data import todos
# interacting through service layer
from service import todo as service

app = FastAPI()


@app.get("/")
def get_todos():
    return service.get_todos()


@app.post("/")
def create_todo():
    return service.create_todo()


@app.patch("/")
def modify_todo():
    return service.modify_todo()


@app.delete("/")
def delete_todo():
    return service.delete_todo()


# run `uvicorn main:app`
