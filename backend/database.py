from sqlalchemy import create_engine
from backend.config import settings


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{settings.database_user}:{settings.database_password}@"
    f"{settings.database_host}:{settings.database_port}/"
    f"{settings.database_name}"
)

engine = create_engine(DATABASE_URL)