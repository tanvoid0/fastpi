from app import app, json, status
from mongoengine import Document, StringField, IntField, ListField, DynamicDocument
from pydantic import BaseModel


class Employee(BaseModel):
    name: str
    age: int
    teams: list


class MongoEmployee(Document):
    name = StringField(max_length=100)
    age = IntField()
    teams = ListField()


@app.get('/api/employee', tags=['Employee'])
def get_all_employees():
    return json.loads(MongoEmployee.objects().to_json())


@app.post('/api/employee', tags=['Employee'], status_code=status.HTTP_201_CREATED)
def create_employee(data: Employee):
    employee = MongoEmployee(name=data.name, age=data.age, teams=data.teams).save()
    return json.loads(employee.to_json())


@app.put('/api/employee/{employee_id}', tags=['Employee'])
def update_employee(employee_id: str, data: Employee):
    employee = MongoEmployee.objects(id=employee_id)
    employee.update(name=data.name, age=data.age, teams=data.teams)
    return json.loads(employee.to_json())
