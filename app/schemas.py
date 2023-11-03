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
<<<<<<< HEAD
       from_attributes = True
=======
        orm_mode = True
>>>>>>> 5ea0e348fc29a4f161900e42e3c2aa6c81fa7f7b
