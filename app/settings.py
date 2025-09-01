from pathlib import Path

from pydantic import DirectoryPath, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 60


class SQLSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASSWORD: str

    @property
    def DATABASE_URL(self):
        return f'postgresql+psycopg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @property
    def ASYNC_DATABASE_URL(self):
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


class Settings(BaseSettings):
    bot_token: str = Field(validation_alias='TELEGRAM_BOT_TOKEN')
    secret_key: str = Field(validation_alias='SECRET_KEY')
    path_to_files: DirectoryPath = Path().absolute() / 'files'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
sql_settings = SQLSettings()

