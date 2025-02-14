from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings

# Create the database engine using the connection URL from the settings
engine = create_engine(settings.DATABASE_URL.replace('postgressql', 'postgresql'))

# Create a sessionmaker that will generate new Session objects bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency to get the database session for FastAPI routes.

    This function creates a new database session, yields it to the route handler, and
    ensures that the session is properly closed after the request is processed.

    Returns:
        Session: The SQLAlchemy session for the database.
    """
    db = SessionLocal()  # Create a new database session
    try:
        yield db  # Yield the session to be used in the route handler
    finally:
        db.close()  # Ensure the session is closed after use
