# Uvicorn Imports
from uvicorn import run as runserver

# FastAPI Imports
from fastapi import FastAPI


# initialize app
app = FastAPI(title="URL Shortener")


@app.get("/")
async def root() -> dict:
    """
    Root api view.
    
    :return: dictionary with a message key
    """
    return {"message": "URL Shortener with FastAPI."}


if __name__ == "__main__":
    runserver(app, host="0.0.0.0", port=3003, reload=True)