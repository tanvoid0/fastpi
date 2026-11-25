class StackModel(BaseModel):
    title: str
    skill: Optional[list]


class Stack(DynamicDocument):
    title: StringField()