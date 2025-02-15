from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from core.config import settings
from typing import Generator

# Create the base for SQLAlchemy models
Base = declarative_base()
# Import all models to create the tables
from models.user import User
from models.course import Course
from models.Lesson import Lesson

class Database:
    """
    Class to manage the PostgreSQL connection using SQLAlchemy.
    """

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URL = (
            f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}"
            f"@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"
        )

        # Create the engine with connection pooling
        self.engine = create_engine(
            self.SQLALCHEMY_DATABASE_URL,
            pool_size=20,                # Maximum number of connections in the pool
            max_overflow=10,             # Additional connections allowed beyond pool_size
            pool_pre_ping=True,          # Checks the connection's health before using it
        )

        # Create a configured session factory
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self) -> Generator[Session, None, None]:
        """
        Provides a new database session.
        Use this method in FastAPI dependencies.

        Returns:
            Session: A new database session.
        """
        db = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()

# Instantiate the Database class
db_instance = Database()

# Create the database tables
Base.metadata.create_all(bind=db_instance.engine)
