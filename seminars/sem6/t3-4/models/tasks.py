import datetime

from pydantic import BaseModel, Field


class TaskIn(BaseModel):
    title: str = Field(..., min_length=2, max_length=40)
    description: str = Field(...)
    done: bool = Field(default=False)


class Task(TaskIn):
    id: int
