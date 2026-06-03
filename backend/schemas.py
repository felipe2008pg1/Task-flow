from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, datetime
from enum import Enum

class StatusEnum(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    done = "done"

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"

# ── Category ──────────────────────────────────────────────
class CategoryBase(BaseModel):
    name: str
    color: str = "#6366f1"

class CategoryCreate(CategoryBase):
    user_id: int

class CategoryOut(CategoryBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True

# ── Task ──────────────────────────────────────────────────
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: StatusEnum = StatusEnum.pending
    priority: PriorityEnum = PriorityEnum.medium
    due_date: Optional[date] = None
    category_id: Optional[int] = None

class TaskCreate(TaskBase):
    user_id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    due_date: Optional[date] = None
    category_id: Optional[int] = None

class TaskOut(TaskBase):
    id: int
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]
    category: Optional[CategoryOut] = None

    class Config:
        from_attributes = True

# ── User ──────────────────────────────────────────────────
class UserBase(BaseModel):
    name: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True