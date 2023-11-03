from fastapi import FastAPI
from .api import todos
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(todos.router)

