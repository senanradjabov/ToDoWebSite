from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.models.base_model import UUIDMixin

if TYPE_CHECKING:
    from app.models.task_model import Task
    from app.models.user_model import User


class TaskUserBase(SQLModel):
    task_id: UUID = Field(foreign_key="task.id", ondelete="CASCADE", nullable=False)
    user_id: UUID = Field(foreign_key="user.id", ondelete="CASCADE", nullable=False)
    can_edit: bool = False


class TaskUser(UUIDMixin, TaskUserBase, table=True):
    task: "Task" = Relationship(back_populates="added_users")
    user: "User" = Relationship(back_populates="added_users")
