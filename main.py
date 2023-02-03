# Uvicorn Imports
from uvicorn import run as runserver

# FastAPI Imports
from fastapi import FastAPI

# Own Imports
from shortener.models import create_tables
from shortener.api_v1 import router as api_v1_router
from shortener.api_v2 import router as api_v2_router


# initialize app
app = FastAPI(title="URL Shortener")

# Include router(s)
app.include_router(api_v1_router, prefix="/v1")
app.include_router(api_v2_router, prefix="/v2")


@app.on_event("startup")
async def startup():
    """
    This function creates the database tables when the server starts.
    """
    await create_tables()


@app.get("/")
async def root() -> dict:
    """
    Root api view.

    :return: dictionary with a message key
    """
    return {"message": "URL Shortener with FastAPI."}


if __name__ == "__main__":
    runserver("main:app", host="0.0.0.0", port=3003, reload=True)
