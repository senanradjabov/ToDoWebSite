from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.models.base_model import IntIDMixin
from app.models.user_model import User

if TYPE_CHECKING:
    from app.models.task_model import Task


class TaskCategoryBase(SQLModel):
    title: str = Field(max_length=32, unique=True)


class TaskCategory(IntIDMixin, TaskCategoryBase, table=True):
    created_by_id: UUID = Field(foreign_key="user.id", ondelete="CASCADE")
    created_by: User = Relationship(back_populates="task_categories")
    tasks: list["Task"] = Relationship(back_populates="category")
