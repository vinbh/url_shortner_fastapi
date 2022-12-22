from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///.shortner.db"

@lru_cache(maxsize=100)
def get_settings():
    settings = Settings()
    print(f"lodaing settings for: {settings.env_name}")
    return settings