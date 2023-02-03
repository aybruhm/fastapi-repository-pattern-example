# Stdlib Imports
from datetime import datetime
from pydantic import BaseModel, HttpUrl


class BaseLinkSchema(BaseModel):
    original: HttpUrl


class CreateLinkSchema(BaseLinkSchema):
    pass


class LinkSchema(BaseLinkSchema):
    id: int
    shortened: HttpUrl
    date_created: datetime

    class Config:
        orm_mode = True
