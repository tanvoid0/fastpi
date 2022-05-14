import datetime

from app import app, json, status, BaseModel
from mongoengine import Document, StringField, IntField, DateTimeField


class TodoModel(BaseModel):
    name: str
    description: str
    deadline: datetime.datetime
    priority: int
    label: str
    date_modified: datetime.datetime


class TodoSchema(Document):
    name = StringField(max_length=200, required=True)
    description = StringField(max_length=500)
    deadline = DateTimeField()
    priority = IntField(default=0)
    label = StringField(default="")
    date_modified = DateTimeField(default=datetime.datetime.utcnow)


@app.get('/api/todo', tags=['Todo'])
def get_all_todos():
    return json.loads(TodoSchema.objects().to_json())


@app.get('/api/todo/{todo_id}', tags=['Todo'])
def get_todo(todo_id: str):
    return json.loads(TodoSchema(id=todo_id).to_json())


@app.post('/api/todo', tags=['Todo'], status_code=status.HTTP_201_CREATED)
def create_todo(data: TodoModel):
    todo = TodoSchema(
        name=data.name,
        description=data.description,
        deadline=data.deadline,
        priority=data.priority,
        label=data.label
    ).save()
    return json.loads(todo.to_json())


@app.put('/api/todo/{todo_id}', tags=['Todo'])
def update_todo(todo_id: str, data: TodoModel):
    todo = TodoSchema.objects(id=todo_id)
    todo.update(
        name=data.name,
        description=data.description,
        deadline=data.deadline,
        priority=data.priority,
        label=data.label
    )
    return json.loads(todo.to_json())


@app.delete('/api/todo/{todo_id}', tags=['Todo'], status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: str):
    TodoSchema(id=todo_id).delete()
    return

