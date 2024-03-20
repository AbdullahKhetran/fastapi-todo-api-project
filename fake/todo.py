from dummy_data import todos as data
from model.todo import Todo


def get_todos() -> list[Todo]:
    return data


def create_todo(todo_item: Todo):
    return {
        "status": "request received",
        "data received": todo_item
    }


def modify_todo(updated_todo: Todo):
    return {
        "status": "request received",
        "updated todo": updated_todo
    }


def delete_todo(todo_id: str):
    return {
        "status": "request received",
        "todo id received": todo_id
    }
