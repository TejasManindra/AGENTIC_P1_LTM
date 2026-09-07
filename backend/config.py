from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Agentic AI for Business Intelligence"
    app_env: str = "development"

    openai_api_key: str = ""

    database_host: str = "localhost"
    database_port: int = 5432
    database_name: str = "agentic_bi"
    database_user: str = ""
    database_password: str = ""

    microsoft_client_id: str = ""
    microsoft_client_secret: str = ""
    microsoft_tenant_id: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()