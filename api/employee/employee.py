from api.lib import *
from api.model_lib import *

router = APIRouter(
    prefix="/api/employee",
    tags=['User'],
    responses={
        404: {
            "description": "Not found"
        }
    }
)


class EmployeeModel(BaseModel):
    name: str
    age: int
    teams: list


class Employee(Document):
    name = StringField(max_length=100)
    age = IntField()
    teams = ListField()


@router.get('/api/employee', tags=['Employee'])
def get_all_employees():
    return json.loads(Employee.objects().to_json())


@router.post('/api/employee', tags=['Employee'], status_code=status.HTTP_201_CREATED)
def create_employee(data: EmployeeModel):
    employee = Employee(name=data.name, age=data.age, teams=data.teams).save()
    return json.loads(employee.to_json())


@router.put('/api/employee/{employee_id}', tags=['Employee'])
def update_employee(employee_id: str, data: EmployeeModel):
    employee = Employee.objects(id=employee_id)
    employee.update(name=data.name, age=data.age, teams=data.teams)
    return json.loads(employee.to_json())
