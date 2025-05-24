import re
import uuid
from datetime import UTC, datetime

from pydantic import BaseModel
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import TIMESTAMP
from sqlalchemy.orm import declared_attr
from sqlmodel import Column, Field
from sqlmodel import SQLModel as _SQLModel


# Taken from https://github.com/Netflix/dispatch/blob/main/src/dispatch/database/core.py
def resolve_table_name(name) -> str:
    """Resolves table names to their mapped names."""
    names = re.split("(?=[A-Z])", name)
    return "_".join([x.lower() for x in names if x])


class SQLModel(_SQLModel):
    @declared_attr.directive
    def __tablename__(cls) -> str:
        return resolve_table_name(cls.__name__)


class IntIDMixin(SQLModel):
    id: int | None = Field(default=None, primary_key=True)


class UUIDMixin(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True)


class CreatedAtMixin(BaseModel):
    created_at: datetime = Field(
        default_factory=datetime.now(UTC),
        sa_column=lambda: Column(TIMESTAMP(timezone=True), nullable=False),
    )


class UpdateAtMixin(SQLModel):
    updated_at: datetime = Field(
        default_factory=datetime.now(UTC),
        sa_column=lambda: Column(
            TIMESTAMP(timezone=True), nullable=False, onupdate=func.now()
        ),
    )


class TimestampMixin(CreatedAtMixin, UpdateAtMixin):
    pass
