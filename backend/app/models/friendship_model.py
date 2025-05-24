from typing import TYPE_CHECKING
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from app.models.base_model import CreatedAtMixin, IntIDMixin
from app.schemas.common_schema import IFriendshipStatusEnum

if TYPE_CHECKING:
    from app.models.user_model import User


class FriendshipBase(SQLModel):
    receiver_id: UUID = Field(foreign_key="user.id")


class Friendship(IntIDMixin, CreatedAtMixin, FriendshipBase, table=True):
    status: IFriendshipStatusEnum = IFriendshipStatusEnum.pending
    sender_id: UUID = Field(foreign_key="user.id", ondelete="CASCADE")

    sender: "User" = Relationship(
        back_populates="sent_requests",
        sa_relationship_kwargs={"foreign_keys": "[Friendship.sender_id]"},
    )
    receiver: "User" = Relationship(
        sa_relationship_kwargs={"foreign_keys": "[Friendship.receiver_id]"},
        back_populates="received_requests",
    )
