from pydantic import BaseModel
from typing import Optional

class TodoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Schema for request on todo creation
class TodoCreate(TodoBase):
    title: str

# Schema for request on todo update
class TodoUpdate(TodoBase):
    pass

# Schema for response
class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True
