# Own Imports
from config.database import SessionLocal


def get_db():
    """
    This function creates a database session,
    yield it to the get_db function, rollback the transaction
    if there's an exception and then finally closes the session.

    Yields:
        db: scoped database session
    """

    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
    finally:
        db.close()
