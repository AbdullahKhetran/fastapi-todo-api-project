from model.todo import Todo
from fake import todo as data


# get todos
sample_todos = [
    {
        "id": "1",
        "title": "lorem",
        "description": "lorem to do"
    },
    {
        "id": "2",
        "title": "ipsum",
        "description": "ipsum to do"
    },
    {
        "id": "3",
        "title": "dolor",
        "description": "dolor to do"
    },
    {
        "id": "4",
        "title": "sit",
        "description": "sit to do"
    },

]


def test_get_todos():
    resp = data.get_todos()
    assert resp == sample_todos


# create todo
sample_body = {
    "id": "string",
    "title": "string",
    "description": "string"
}

sample_response_for_create_todo = {
    "status": "request received",
    "data received": sample_body
}


def test_create_todo():
    resp = data.create_todo(sample_body)
    assert resp == sample_response_for_create_todo


# modify todo
sample_response_for_modify_todo = {
    "status": "request received",
    "updated todo": sample_body
}


def test_modify_todo():
    resp = data.modify_todo(sample_body)
    assert resp == sample_response_for_modify_todo


# delete todo
sample_id: str = "3"

sample_response_for_delete_todo = {
    "status": "request received",
    "todo id received": sample_id
}


def test_delete_todo():
    resp = data.delete_todo(sample_id)
    assert resp == sample_response_for_delete_todo
