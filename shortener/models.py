# Stdlib Imports
from datetime import datetime

# SQLAlchemy Imports
from sqlalchemy import Column, String, Integer, DateTime

# Own Imports
from config.database import Base, DATABASE_ENGINE


async def create_tables():
    Link.metadata.create_all(bind=DATABASE_ENGINE)


class Link(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True, index=True)
    original = Column(String)
    shortened = Column(String(4))
    date_created = Column(DateTime, default=datetime.now)
    date_modified = Column(DateTime, onupdate=datetime.now)

    def __str__(cls) -> str:
        """
        `__str__` is a special method that returns a string representation of an object.

        :param cls: The class object
        :return: The shortened version of the original link
        """
        return cls.shortened.__str__()
