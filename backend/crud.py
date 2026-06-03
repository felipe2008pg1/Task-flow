from sqlalchemy.orm import Session
from models import Task, Category, User
from schemas import TaskCreate, TaskUpdate, CategoryCreate, UserCreate

# ── Users ──────────────────────────────────────────────────
def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# ── Categories ─────────────────────────────────────────────
def get_categories(db: Session, user_id: int):
    return db.query(Category).filter(Category.user_id == user_id).all()

def create_category(db: Session, category: CategoryCreate):
    db_cat = Category(**category.model_dump())
    db.add(db_cat)
    db.commit()
    db.refresh(db_cat)
    return db_cat

def delete_category(db: Session, category_id: int):
    cat = db.query(Category).filter(Category.id == category_id).first()
    if cat:
        db.delete(cat)
        db.commit()
    return cat

# ── Tasks ──────────────────────────────────────────────────
def get_tasks(db: Session, user_id: int, status: str = None, priority: str = None):
    q = db.query(Task).filter(Task.user_id == user_id)
    if status:
        q = q.filter(Task.status == status)
    if priority:
        q = q.filter(Task.priority == priority)
    return q.order_by(Task.created_at.desc()).all()

def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()

def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, task_data: TaskUpdate):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        return None
    for field, value in task_data.model_dump(exclude_unset=True).items():
        setattr(task, field, value)
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

def get_stats(db: Session, user_id: int):
    total = db.query(Task).filter(Task.user_id == user_id).count()
    pending = db.query(Task).filter(Task.user_id == user_id, Task.status == "pending").count()
    in_progress = db.query(Task).filter(Task.user_id == user_id, Task.status == "in_progress").count()
    done = db.query(Task).filter(Task.user_id == user_id, Task.status == "done").count()
    return {"total": total, "pending": pending, "in_progress": in_progress, "done": done}