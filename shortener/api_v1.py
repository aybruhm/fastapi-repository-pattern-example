# FastAPI Imports
from fastapi import APIRouter

# Own Imports
from shortener.schemas import CreateLinkSchema
from shortener.services import create_shortened_link, redirect_to_original_link


# Initialize api router
router = APIRouter(tags=["API v1"])


@router.post("/shorten/", status_code=201)
async def shorten_url(payload: CreateLinkSchema):
    """
    This API view is responsible for shortening a link.

    :param payload: CreateLinkSchema ({"original": "string"})\n
    :type payload: Pydantic Model

    :return: A dictionary containing a message and link serialized data.
    """

    link = await create_shortened_link(payload.original)
    return {"message": "Link shortened!", "data": link}


@router.get("/{code}/")
async def redirect_code(code: str):
    """
    This API view takes the shortened link code as a parameter,
    and redirects the user to the original link.

    :param code: str = the shortened code of the original link
    :type code: str

    :return: redirect to original link
    """

    original_link = await redirect_to_original_link(code)
    return original_link
