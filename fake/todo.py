from dummy_data import todos as data
from model.todo import Todo


def get_todos() -> list[Todo]:
    return data


def create_todo(todo_item: Todo):
    return "Todo created"


def modify_todo(todo_id: int, updated_todo: Todo):
    return "Todo modified"


def delete_todo(todo_id: int):
    return "Todo deleted"
