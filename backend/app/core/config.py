from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    database_url: str
    openai_api_key: str
    environment: str = "development"
    
    # Embedding configuration
    embedding_model: str = "text-embedding-3-small"
    embedding_dimensions: int = 1536
    
    class Config:
        env_file = ".env"


settings = Settings()
