# SQLAlchemy Imports
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Construct database type and engine
DATABASE_URL = "sqlite:///./shortener.sqlite"
DATABASE_ENGINE = create_engine(
    url=DATABASE_URL, connect_args={"check_same_thread": False}
)

# Construct a session maker
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=DATABASE_ENGINE
)

# Construct a base class for declarative class definitions.
Base = declarative_base()
