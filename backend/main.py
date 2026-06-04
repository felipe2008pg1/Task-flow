from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional, List
from backend import models, crud, schemas
from backend.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="TaskFlow API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── Health Check ───────────────────────────────────────────
@app.get("/")
def root():
    return {"message": "TaskFlow API online 🚀"}

# ── Users ──────────────────────────────────────────────────
@app.get("/users", response_model=List[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/users", response_model=schemas.UserOut, status_code=201)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    novo_usuario = crud.create_user(db, user)
    if not novo_usuario:
        raise HTTPException(status_code=400, detail="Este e-mail já está cadastrado no sistema.")
    return novo_usuario

# ── Categories ─────────────────────────────────────────────
@app.get("/users/{user_id}/categories", response_model=List[schemas.CategoryOut])
def list_categories(user_id: int, db: Session = Depends(get_db)):
    return crud.get_categories(db, user_id)

@app.post("/categories", response_model=schemas.CategoryOut, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    nova_categoria = crud.create_category(db, category)
    if not nova_categoria:
        raise HTTPException(status_code=404, detail="Não é possível criar a categoria. Usuário não encontrado.")
    return nova_categoria

@app.delete("/categories/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = crud.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")

# ── Tasks ──────────────────────────────────────────────────
@app.get("/users/{user_id}/tasks", response_model=List[schemas.TaskOut])
def list_tasks(
    user_id: int,
    status: Optional[str] = Query(None),
    priority: Optional[str] = Query(None),
    db: Session = Depends(get_db),
):
    return crud.get_tasks(db, user_id, status, priority)

@app.post("/tasks", response_model=schemas.TaskOut, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    resultado = crud.create_task(db, task)
    if isinstance(resultado, dict) and "error" in resultado:
        if resultado["error"] == "user_not_found":
            raise HTTPException(status_code=404, detail="Usuário não encontrado.")
        if resultado["error"] == "invalid_category":
            raise HTTPException(status_code=400, detail="A categoria informada não existe ou não pertence a este usuário.")
    return resultado

@app.patch("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task_data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    resultado = crud.update_task(db, task_id, task_data)
    if not resultado:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    if isinstance(resultado, dict) and "error" in resultado:
        if resultado["error"] == "invalid_category":
            raise HTTPException(status_code=400, detail="A categoria informada não pertence a este usuário.")
    return resultado

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.get("/users/{user_id}/stats")
def get_stats(user_id: int, db: Session = Depends(get_db)):
    return crud.get_stats(db, user_id)