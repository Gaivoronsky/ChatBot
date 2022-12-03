from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'postgresql://alex:hardpassword@postgres:5432/analyzedb'


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
