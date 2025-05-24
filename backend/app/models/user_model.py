from typing import TYPE_CHECKING
from uuid import UUID

from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel

from app.models.base_model import TimestampMixin, UUIDMixin

if TYPE_CHECKING:
    from app.models.friendship_model import Friendship
    from app.models.task_category_model import TaskCategory
    from app.models.task_model import Task
    from app.models.task_user_model import TaskUser


class UserBase(SQLModel):
    email: EmailStr
    first_name: str = Field(max_length=32)
    last_name: str = Field(max_length=32)
    is_superuser: bool = Field(default=False)
    is_active: bool = Field(default=True)


class User(UUIDMixin, TimestampMixin, UserBase, table=True):
    hashed_password: str = Field(max_length=64)
    image_id: UUID | None = None

    task_categories: list["TaskCategory"] = Relationship(back_populates="created_by")
    sent_requests: list["Friendship"] = Relationship(
        back_populates="sender",
        sa_relationship_kwargs={"foreign_keys": "[Friendship.sender_id]"},
    )
    received_requests: list["Friendship"] = Relationship(
        back_populates="receiver",
        sa_relationship_kwargs={"foreign_keys": "[Friendship.receiver_id]"},
    )
    tasks: list["Task"] = Relationship(back_populates="creator_by")
    added_tasks: list["TaskUser"] = Relationship(back_populates="user")
