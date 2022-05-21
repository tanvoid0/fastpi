from api.lib import *

from api.todo.todo import Todo, TodoModel

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

