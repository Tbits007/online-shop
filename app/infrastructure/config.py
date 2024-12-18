from typing import Literal
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_token_secret: str
    verification_token_secret: str


class Settings(BaseSettings):
    MODE: Literal["DEV", "TEST", "PROD"]
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]

    DB_HOST: str 
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    TEST_DB_HOST: str 
    TEST_DB_PORT: int
    TEST_DB_USER: str
    TEST_DB_PASS: str
    TEST_DB_NAME: str
       
    access_token: AccessToken
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


    @property
    def TEST_DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.TEST_DB_USER}:{self.TEST_DB_PASS}@{self.TEST_DB_HOST}:{self.TEST_DB_PORT}/{self.TEST_DB_NAME}"


settings = Settings()
