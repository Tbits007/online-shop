from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600


class Settings(BaseSettings):
    DB_HOST: str 
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    
    access_token: AccessToken = AccessToken()

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

    @property
    def DATABASE_URL(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
