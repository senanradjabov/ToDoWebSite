from enum import Enum

from pydantic import PostgresDsn, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModeEnum(str, Enum):
    development: str = "development"
    production: str = "production"
    testing: str = "testing"


class Settings(BaseSettings):
    # App Mode
    MODE: ModeEnum = ModeEnum.development

    # PostgreSQL
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    ASYNC_POSTGRES_URL: PostgresDsn | str = ""

    @field_validator("ASYNC_POSTGRES_URL", mode="after")
    def assemble_async_postgres_url(cls, v: str, info: FieldValidationInfo) -> str:
        if not v:
            return PostgresDsn.build(
                scheme="postgresql+asyncpg",
                username=info.data["POSTGRES_USER"],
                password=info.data["POSTGRES_PASSWORD"],
                host=info.data["POSTGRES_HOST"],
                port=info.data["POSTGRES_PORT"],
                path=info.data["POSTGRES_DB"],
            )

        return v

    model_config = SettingsConfigDict(
        env_file="../.env",
        env_file_encoding="utf-8",
    )


settings = Settings()
