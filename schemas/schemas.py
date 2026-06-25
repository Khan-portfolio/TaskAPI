from pydantic import BaseModel

class TaskAddScheme(BaseModel):
    name:str
    status: bool

class TaskScheme(TaskAddScheme):
    id:int