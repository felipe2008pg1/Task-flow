from sqlalchemy import Column, Integer, String, Text, Enum, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    tasks = relationship("Task", back_populates="user", cascade="all, delete")
    categories = relationship("Category", back_populates="user", cascade="all, delete")


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), nullable=False)
    color = Column(String(7), default="#6366f1")
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, server_default=func.now())

    user = relationship("User", back_populates="categories")
    tasks = relationship("Task", back_populates="category")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    status = Column(Enum("pending", "in_progress", "done"), default="pending")
    priority = Column(Enum("low", "medium", "high"), default="medium")
    due_date = Column(Date, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")