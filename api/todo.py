import datetime
import json
from typing import Optional

from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField
from pydantic import BaseModel, Field
from fastapi import status, APIRouter


class TodoModel(BaseModel):
    name: str
    description: Optional[str]
    deadline: Optional[datetime.datetime]
    priority: Optional[int]
    label: Optional[str]
    done: Optional[bool] = Field(default=False)


class Todo(Document):
    name = StringField(max_length=200, required=True)
    description = StringField(max_length=500)
    deadline = DateTimeField()
    priority = IntField(default=0)
    label = StringField(default="")
    done = BooleanField(default=False)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)


router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"],
)


@router.get('/')
def get_all_todos():
    return json.loads(Todo.objects().to_json())


@router.get('/api/todo/{todo_id}')
def get_todo(todo_id: str):
    return json.loads(Todo(id=todo_id).to_json())


@router.post('/api/todo')
def create_todo(data: TodoModel):
    todo = Todo(
        name=data.name,
        description=data.description,
        deadline=data.deadline,
        priority=data.priority,
        label=data.label
    ).save()
    return json.loads(todo.to_json())


@router.put('/{todo_id}')
def update_todo(todo_id: str, data: TodoModel):
    todo = Todo.objects(id=todo_id)
    todo.update(
        name=data.name,
        description=data.description,
        deadline=data.deadline,
        priority=data.priority,
        label=data.label
    )
    return json.loads(todo.to_json())


@router.delete('/{todo_id}')
def delete_todo(todo_id: str):
    Todo(id=todo_id).delete()
    return

