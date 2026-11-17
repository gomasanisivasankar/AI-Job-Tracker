from pydantic_settings import BaseSettings,SettingsConfigDict
from sqlalchemy import URL
class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env",env_file_encoding="utf-8")
    app_name:str="AI Job Tracker"

    # Database settings
    POSTGRES_USER:str
    POSTGRES_PASSWORD:str
    POSTGRES_DB:str
    POSTGRES_HOST:str="localhost"
    POSTGRES_PORT:int=5433

    @property
    def database_url(self)->URL:
        database_url=URL.create(
            drivername="postgresql+asyncpg",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            database=self.POSTGRES_DB
        )
        return database_url
#read and check the settings from the .env file
settings=Settings()
