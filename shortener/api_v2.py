# Stdlib Imports
import random
import string

# FastAPI Imports
from fastapi import APIRouter, Path, Depends
from fastapi.responses import RedirectResponse

# SQLAlchemy Imports
from sqlalchemy.orm import Session

# Own Imports
from config.deps import get_db
from shortener.models import Link
from shortener.schemas import CreateLinkSchema


# Initialize api router
router = APIRouter(tags=["API v2"])


@router.post("/shorten/", status_code=201)
async def shorten_url(
    payload: CreateLinkSchema, db: Session = Depends(get_db)
):
    shortened_link = "".join(
        random.choice(string.ascii_letters) for i in range(4)
    )
    link = Link(original=payload.original, shortened=shortened_link)

    db.add(link)
    db.commit()
    db.refresh(link)

    return {"message": "Link shortened!", "data": link}


@router.get("/{code}/")
async def redirect_code(code: str = Path(), db: Session = Depends(get_db)):
    link = db.query(Link).filter_by(shortened=code).first()
    return RedirectResponse(link.original)
