import os

from dotenv import load_dotenv

# env_path = Path(__file__).parent / ".env"
load_dotenv()


class Settings:
    PROJECT_NAME: str = "Agent Server"
    PROJECT_VERSION: str = "1.0.0"

    DATABASE_URL: str = os.getenv("DATABASE_URL")
    ACCESS_TOKEN_KEY = os.getenv("ACCESS_TOKEN_KEY")
    REFRESH_TOKEN_KEY = os.getenv("REFRESH_TOKEN_KEY")
    ALGORITHM = os.getenv("ALGORITHM")

    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 30


settings = Settings()
