import datetime
import json
from typing import Optional

from mongoengine import Document, StringField, IntField, DateTimeField, BooleanField, ReferenceField
from pydantic import BaseModel, Field
from fastapi import status, APIRouter, Depends, HTTPException

from api.auth.utility import JWTBearer, get_id_from_jwt
from api.user import User


class TodoModel(BaseModel):
    name: str = Field(description="Enter Task")
    description: Optional[str] = Field()
    deadline: Optional[datetime.datetime] = Field()
    priority: Optional[int] = Field()
    label: Optional[str] = Field()
    done: Optional[bool] = Field(default=False)


class Todo(Document):
    name = StringField(max_length=200, required=True)
    description = StringField(max_length=500)
    deadline = DateTimeField()
    priority = IntField(default=0)
    label = StringField(default="")
    done = BooleanField(default=False)
    date_modified = DateTimeField(default=datetime.datetime.utcnow)
    user = ReferenceField(User)


router = APIRouter(
    prefix="/api/todo",
    tags=["Todo"],
)


@router.get('/')
def get_all_todos():
    return json.loads(Todo.objects().to_json())


@router.get('/{todo_id}')
def get_todo(todo_id: str):
    return json.loads(Todo(id=todo_id).to_json())


@router.post('/')
def create_todo(data: TodoModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    todo = Todo(
        name=data.name,
        description=data.description,
        deadline=data.deadline,
        priority=data.priority,
        label=data.label,
        user=user
    ).save()
    return json.loads(todo.to_json())


@router.put('/{todo_id}')
def update_todo(todo_id: str, data: TodoModel, token: str = Depends(JWTBearer())):
    user = get_id_from_jwt(token)
    todo = Todo.objects(id=todo_id).get()
    if user != str(todo.user.pk):
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User is not allowed to update the data")
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

