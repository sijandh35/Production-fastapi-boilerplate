from sqlalchemy import create_engine, inspect
from langchain_community.utilities import SQLDatabase
from sqlalchemy.orm import sessionmaker,declarative_base

from config import settings

# Database connection
db_user = settings.db_user       
db_password = settings.db_password
db_host = settings.db_host
db_name = settings.db_name
db_port = settings.db_port

# Database URL
DATABASE_URL = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create engine and session
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sql_database = SQLDatabase(engine)
print("database connected")
inspector = inspect(engine)

#base class for models
Base = declarative_base()
# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

