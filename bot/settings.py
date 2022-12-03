from pydantic import BaseSettings


class Settings(BaseSettings):
    database_url: str = 'postgresql://alex:hardpassword@postgres:5432/analyzedb'
    name_model: str = 'inkoziev/rugpt_chitchat'
    is_docker: bool = True
    max_len_history: int = 10
    start_len_history: int = 3
    api_id: int
    api_hash: str
    phone: str
    chat_id: int
    my_id: int


settings = Settings(
    _env_file='.env',
    _env_file_encoding='utf-8',
)
