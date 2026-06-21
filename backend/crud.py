from sqlalchemy.orm import Session
from backend.models import User, Category, Task
from backend.schemas import UserCreate, CategoryCreate, TaskCreate, TaskUpdate

# ── USER OPERATIONS ───────────────────────────────────
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user: UserCreate):
    if get_user_by_email(db, user.email):
        return None  # Indicates a duplicate email conflict.
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ── CATEGORY OPERATIONS ─────────────────────────────────
def get_categories(db: Session, user_id: int):
    return db.query(Category).filter(Category.user_id == user_id).all()

def create_category(db: Session, category: CategoryCreate):
    if not get_user(db, category.user_id):
        return None  # Indicates that the owner user does not exist.
    db_category = Category(name=category.name, user_id=category.user_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = db.query(Category).filter(Category.id == category_id).first()
    if db_category:
        db.delete(db_category)
        db.commit()
        return True
    return False

# ── TASK OPERATIONS ─────────────────────────────────────
def get_tasks(db: Session, user_id: int, status: str = None, priority: str = None):
    query = db.query(Task).filter(Task.user_id == user_id)
    if status:
        query = query.filter(Task.status == status)
    if priority:
        query = query.filter(Task.priority == priority)
    return query.all()

def create_task(db: Session, task: TaskCreate):
    if not get_user(db, task.user_id):
        return {"error": "user_not_found"}
        
    if task.category_id:
        category = db.query(Category).filter(
            Category.id == task.category_id, 
            Category.user_id == task.user_id
        ).first()
        if not category:
            return {"error": "invalid_category"}

    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        return None
    
    update_dict = task_data.model_dump(exclude_unset=True)
    
    if "category_id" in update_dict and update_dict["category_id"] is not None:
        category = db.query(Category).filter(
            Category.id == update_dict["category_id"], 
            Category.user_id == db_task.user_id
        ).first()
        if not category:
            return {"error": "invalid_category"}

    for key, value in update_dict.items():
        setattr(db_task, key, value)
        
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
        return True
    return False

# ── STATISTICS ───────────────────────────────────────────
def get_stats(db: Session, user_id: int):
    total = db.query(Task).filter(Task.user_id == user_id).count()
    completed = db.query(Task).filter(Task.user_id == user_id, Task.status == "Concluída").count()
    pending = db.query(Task).filter(Task.user_id == user_id, Task.status == "Pendente").count()
    in_progress = db.query(Task).filter(Task.user_id == user_id, Task.status == "Em Progresso").count()
    
    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "in_progress_tasks": in_progress,
        "completion_rate": (completed / total * 100) if total > 0 else 0
    }
