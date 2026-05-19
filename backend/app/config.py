from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "RSOD Platform"
    VERSION: str = "1.0.0"

    # 数据库
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    DB_USER: str = "rsod_user"
    DB_PASSWORD: str = "rsod_password"
    DB_NAME: str = "rsod_db"

    # Redis
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379

    # MinIO
    MINIO_HOST: str = "localhost:9000"
    MINIO_ACCESS_KEY: str = "minioadmin"
    MINIO_SECRET_KEY: str = "minioadmin"
    MINIO_BUCKET: str = "rsod-bucket"

settings = Settings()