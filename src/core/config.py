from functools import lru_cache
import os
from pathlib import Path
from typing import Dict, List
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


# Get the absolute path of the `.env` file in the current project
BASE_DIR = Path(__file__).resolve().parent.parent.parent  # Gets `app/` folder
ENV_FILE_PATH = BASE_DIR / ".env"  # Looks for `.env` in the project root

class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        env_file=".env"
    )

    LOG_LEVEL: str = Field(default="INFO")
    KB_AGENT_BASE_URL: str
    
    # Redis Configurations
    REDIS_HOST: str = Field(default="localhost")
    REDIS_PORT: int = Field(default=6379)
    REDIS_INDEX: int = Field(default=1)

    # Telegram Configurations
    TELEGRAM_BASE_URL: str
    TELEGRAM_BOT_TOKEN: str
    TELEGRAM_BOT_NAME: str
    CONCURRENT_UPDATES: int = Field(default=256)
    POOL_TIMEOUT: int = Field(default=30)
    CONNECTION_POOL_SIZE: int = Field(default=1024)
    CONNECT_TIMEOUT: int = Field(default=300)
    READ_TIMEOUT: int = Field(default=15)
    WRITE_TIMEOUT: int = Field(default=10)
    UVICORN_WORKERS: int = Field(default=4)
   

    WELCOME_MSG: str = "Namaste 🙏\nWelcome to *KB Support Assistant*\n_(Powered by Bhashini)_"
    DEFAULT_LANGUAGE: str = Field(default="en")
    SUPPORTED_LANGUAGES: str = Field(default="en,bn,gu,hi,kn,ml,mr,or,pa,ta,te")
    LANGUAGES: List[Dict] = [
        {"text": "English", "code": "en", "index": 1},
        {"text": "বাংলা", "code": "bn", "index": 2},
        {"text": "ગુજરાતી", "code": "gu", "index": 3},
        {"text": "हिंदी", "code": "hi", "index": 4},
        {"text": "ಕನ್ನಡ", "code": "kn", "index": 5},
        {"text": "മലയാളം ", "code": "ml", "index": 6},
        {"text": "मराठी", "code": "mr", "index": 7},
        {"text": "ଓଡ଼ିଆ", "code": "or", "index": 8},
        {"text": "ਪੰਜਾਬੀ", "code": "pa", "index": 9},
        {"text": "தமிழ்", "code": "ta", "index": 10},
        {"text": "తెలుగు", "code": "te", "index": 11}
    ]

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()