from fastapi import FastAPI
from .api import todos
from . import models
from .database import engine
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Serve the index.html file at the root URL
@app.get("/")
async def root():
    return FileResponse('static/index.html')


# Mount the static directory to be served at '/static'
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(todos.router)


