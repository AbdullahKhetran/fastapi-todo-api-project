from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def greet():
    return "Hello"

# run `uvicorn main:app`
