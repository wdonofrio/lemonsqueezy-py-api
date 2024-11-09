from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """API Settings Object"""

    api_key: str
    api_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
