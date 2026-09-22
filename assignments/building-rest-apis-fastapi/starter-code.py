from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks API")


class TaskCreate(BaseModel):
    """Dados necessários para criar ou atualizar uma tarefa."""

    title: str = Field(min_length=1)
    completed: bool = False


class Task(TaskCreate):
    """Formato completo de uma tarefa armazenada."""

    id: int


# Use esta lista em memória como banco de dados durante a atividade.
tasks: list[Task] = []


@app.get("/")
def read_root():
    """Retorne uma mensagem confirmando que a API está funcionando."""
    pass


@app.get("/tasks", response_model=list[Task])
def list_tasks():
    """Retorne todas as tarefas cadastradas."""
    pass


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    """Crie uma tarefa e atribua um identificador único."""
    pass


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    """Retorne uma tarefa pelo identificador."""
    pass


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskCreate):
    """Atualize uma tarefa existente."""
    pass


@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Exclua uma tarefa existente."""
    pass
