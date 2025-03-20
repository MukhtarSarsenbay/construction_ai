from pydantic import BaseModel
from datetime import datetime

class ProjectCreate(BaseModel):
    project_name: str
    location: str

class TaskSchema(BaseModel):
    name: str
    status: str

class ProjectResponse(BaseModel):
    id: int
    project_name: str
    location: str
    status: str
    created_at: datetime
    tasks: list[TaskSchema]