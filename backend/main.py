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
    new_user = crud.create_user(db, user)
    if not new_user:
        raise HTTPException(status_code=400, detail="This email is already registered in the system.")
    return new_user

# ── Categories ─────────────────────────────────────────────
@app.get("/users/{user_id}/categories", response_model=List[schemas.CategoryOut])
def list_categories(user_id: int, db: Session = Depends(get_db)):
    return crud.get_categories(db, user_id)

@app.post("/categories", response_model=schemas.CategoryOut, status_code=201)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    new_category = crud.create_category(db, category)
    if not new_category:
        raise HTTPException(status_code=404, detail="Unable to create category. User not found.")
    return new_category

@app.delete("/categories/{category_id}", status_code=204)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    success = crud.delete_category(db, category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")

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
    result = crud.create_task(db, task)
    if isinstance(result, dict) and "error" in result:
        if result["error"] == "user_not_found":
            raise HTTPException(status_code=404, detail="User not found.")
        if result["error"] == "invalid_category":
            raise HTTPException(status_code=400, detail="The specified category does not exist or does not belong to this user.")
    return result

@app.patch("/tasks/{task_id}", response_model=schemas.TaskOut)
def update_task(task_id: int, task_data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    result = crud.update_task(db, task_id, task_data)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    if isinstance(result, dict) and "error" in result:
        if result["error"] == "invalid_category":
            raise HTTPException(status_code=400, detail="The specified category does not belong to this user.")
    return result

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    success = crud.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")

@app.get("/users/{user_id}/stats")
def get_stats(user_id: int, db: Session = Depends(get_db)):
    return crud.get_stats(db, user_id)
