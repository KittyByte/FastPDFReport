from pydantic import Field, DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path


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
    files_dir: DirectoryPath = Path().absolute() / 'files'

    model_config = SettingsConfigDict(env_file='.env', extra='ignore')


settings = Settings()
sql_settings = SQLSettings()

