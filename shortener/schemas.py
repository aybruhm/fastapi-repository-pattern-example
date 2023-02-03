# Stdlib Imports
from datetime import datetime
from pydantic import BaseModel


class BaseLinkSchema(BaseModel):
    shortened: str


class CreateLinkSchema(BaseLinkSchema):
    pass


class LinkSchema(BaseLinkSchema):
    id: int
    shortened: str
    date_created: datetime

    class Config:
        orm_mode = True
