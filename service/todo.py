import fake.todo as data
from model.todo import Todo


# Service layer interacting with data layer
def get_todos() -> list[Todo]:
    return data.get_todos()


def create_todo(todo_item: Todo):
    return data.create_todo(todo_item)


def modify_todo(todo_id: int, updated_todo: Todo):
    return data.modify_todo()


def delete_todo(todo_id):
    return data.delete_todo(todo_id)
