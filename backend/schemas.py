from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

# ── USER SCHEMAS ───────────────────────────────────────────
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

# ── CATEGORY SCHEMAS ───────────────────────────────────────
class CategoryBase(BaseModel):
    name: str
    user_id: int

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
    name: str
    user_id: int

    class Config:
        from_attributes = True

# ── TASK SCHEMAS ───────────────────────────────────────────
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "Pending"
    priority: Optional[str] = "Medium"
    due_date: Optional[datetime] = None
    user_id: int
    category_id: Optional[int] = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    priority: Optional[str] = None
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None

class TaskOut(TaskBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True
