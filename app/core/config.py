from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()


# Application configuration class using Pydantic BaseSettings
class AppConfig(BaseSettings):
    # Secret key for signing JWT tokens
    SECRET_KEY: str
    # Algorithm used for signing JWT tokens
    ALGORITHM: str = "HS256"
    # Token expiration time (in minutes)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    # API key for the external service
    API_KEY: str

    # Configuration dictionary for specifying environment file
    model_config = SettingsConfigDict(env_file=".env")
