# Stdlib Imports
from typing import List

# SQLAlchemy Imports
from sqlalchemy.orm import Session

# Own Imports
from config.deps import get_db
from shortener.models import Link


class LinkRepository:
    """Repository responsible for performing operations (CRUD, etc) on links table."""

    def __init__(self) -> None:
        self.db: Session = get_db().__next__()

    async def create(self, original: str, shortened: str) -> Link:
        """
        This method is responsible for creating a new link object.

        :param original: original url link
        :param shortened: shortened url link

        :return: the link object
        """

        link = Link(original=original, shortened=shortened)

        self.db.add(link)
        self.db.commit()
        self.db.refresh(link)

        return link

    async def get(self, skip: int, end: int) -> List[Link]:
        """
        This method retrieves a list of links objects.

        :param skip: The number of links to skip
        :type skip: int

        :param end: The number of links to retrieve
        :type end: int

        :return: A list of link objects
        """

        links = self.db.query(Link).offset(skip).limit(end).all()
        return links


link_repository = LinkRepository()
