from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str
    LOG_LEVEL: str = "INFO"
    API_VERSION: str = "/api/v1"

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()