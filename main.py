from fastapi import FastAPI
from dummy_data import todos

app = FastAPI()


@app.get("/")
def get_todo():
    return todos


# run `uvicorn main:app`
