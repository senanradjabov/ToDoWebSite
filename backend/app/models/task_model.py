from datetime import datetime
from typing import TYPE_CHECKING, Optional
from uuid import UUID

from sqlmodel import Column, DateTime, Field, Relationship, SQLModel

from app.models.base_model import TimestampMixin, UUIDMixin
from app.schemas.common_schema import ITaskPriorityEnum, ITaskStatusEnum

if TYPE_CHECKING:
    from app.models.task_category_model import TaskCategory
    from app.models.task_user_model import TaskUser
    from app.models.user_model import User


class TaskBase(SQLModel):
    title: str = Field(max_length=256)
    description: str
    category_id: int | None = Field(
        default=None, foreign_key="task_category.id", ondelete="SET NULL", nullable=True
    )
    deu_date: datetime = Field(
        sa_column=Column(DateTime(timezone=True), nullable=False),
    )
    priority: ITaskPriorityEnum
    status: ITaskStatusEnum


class Task(UUIDMixin, TimestampMixin, TaskBase, table=True):
    image_id: UUID | None = None
    creator_by_id: UUID = Field(foreign_key="user.id", ondelete="CASCADE")

    category: Optional["TaskCategory"] | None = Relationship(back_populates="tasks")
    creator_by: "User" = Relationship(back_populates="tasks")
    added_users: list["TaskUser"] = Relationship(back_populates="task")
