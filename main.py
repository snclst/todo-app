from uuid import uuid4

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
)

tasks: list[TaskSchema] = []
books = []

class TaskSchema(BaseModel):
    id: str
    title: str
    completed: bool

class TaskCreateSchema(BaseModel):
    title: str

class BookSchema(BaseModel):
    book: str

@app.get('/tasks')
def read_tasks():
    return {"message": f"Любимая книга: {books}"}

@app.post('/tasks')
def create_task(payload: TaskCreateSchema) -> TaskSchema:
    new_task = TaskSchema(id=str(uuid4), title=payload.title, completed=False)
    tasks.append(new_task)
    return new_task

@app.post('/book')
def add_book(payload: BookSchema) -> None:
    new_book = BookSchema(book=payload.book)
    books.append(new_book)
    return new_book
