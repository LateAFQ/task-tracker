import os
from pathlib import Path
from typing import (
    Final,
    List,
    Optional,
    Union,
)

from dotenv import find_dotenv, load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv(find_dotenv(raise_error_if_not_found=True))

_PathLike = Union[os.PathLike[str], str, Path]


LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
PROJECT_NAME = os.getenv("PROJECT_NAME", "")
PROJECT_VERSION = os.getenv("PROJECT_VERSION", "")

LOGGING_FORMAT: Final[str] = "%(asctime)s %(name)s %(levelname)s -> %(message)s"
DATETIME_FORMAT: Final[str] = "%Y.%m.%d %H:%M"


class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    POSTGRES_URI: str
    POSTGRES_DB: str
    POSTGRES_HOST: Optional[str] = None
    POSTGRES_PORT: Optional[int] = None
    POSTGRES_USER: Optional[str] = None
    POSTGRES_PASSWORD: Optional[str] = None

    @property
    def url(self) -> str:
        return self.POSTGRES_URI.format(
            self.POSTGRES_USER,
            self.POSTGRES_PASSWORD,
            self.POSTGRES_HOST,
            self.POSTGRES_PORT,
            self.POSTGRES_DB,
        )


class ServerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./.env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        env_prefix="SERVER_",
        extra="ignore",
    )

    host: str = "127.0.0.1"
    port: int = 8080


class Settings(BaseSettings):
    #db: DatabaseSettings
    server: ServerSettings


def load_settings(
    #db: Optional[DatabaseSettings] = None,
    server: Optional[ServerSettings] = None,
) -> Settings:
    return Settings(
        #db=db or DatabaseSettings(),
        server=server or ServerSettings(),
    )