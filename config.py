from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "API"
    
    # Database settings
    db_user: str
    db_password: str
    db_host: str
    db_name: str
    db_port: str
    
    # AWS settings
    aws_access_key_id: str
    aws_secret_access_key: str
    aws_default_region: str
    
    # API Keys
    mistral_api_key: str
    backend_url: str 
    MONGO_COLLECTION: str
    MONGO_INITDB_DATABASE: str
    MONGO_ENDPOINT: str
    REDIS_URL: str
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str

    class Config:
        env_file = "envs/.env" 
        extra = "allow"

# Instantiate the settings
settings = Settings()

