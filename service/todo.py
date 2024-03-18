import fake.todo as data


# Service layer interacting with data layer
def get_todos():
    return data.get_todos()


def create_todo():
    return data.create_todo()


def modify_todo():
    return data.modify_todo()


def delete_todo():
    return data.delete_todo()
