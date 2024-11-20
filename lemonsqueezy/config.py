from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """API Settings Object"""

    api_key: str = Field(..., alias="LEMONSQUEEZY_API_KEY")
    api_url: str = Field(..., alias="LEMONSQUEEZY_API_URL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
