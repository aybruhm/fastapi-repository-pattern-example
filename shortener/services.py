# Stdlib Imports
import random
import string

# Own Imports
from shortener.repository import link_repository, Link


async def shorten_link() -> str:
    """
    This function returns a random string of 4 characters.

    :return: A string of 4 random letters.
    """
    shrt_str = "".join(random.choice(string.ascii_letters, k=4))
    return shrt_str


async def create_shortened_link(original: str) -> Link:
    """
    This function creates a shortened link for the given original link.

    :param original: str - the original link that we want to shorten
    :type original: str

    :return: A Link object
    """
    
    shortened_link = await shorten_link()
    link = await link_repository.create(original, shortened_link)
    return link
