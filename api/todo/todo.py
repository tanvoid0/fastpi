from api.model_lib import *
from api.user.user import UserSchema


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
    user = ReferenceField(UserSchema)

