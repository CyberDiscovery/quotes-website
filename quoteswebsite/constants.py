import base64
from os import environ


def getenv(name: str, fallback: str = "") -> str:
    """Return an (optionally base64-encoded) env var."""
    variable = environ.get(name)
    if bool(environ.get("DEPLOY")) and variable is not None:
        variable = base64.b64decode(variable).decode()
    return variable or fallback


class PostgreSQL:
    PGHOST = getenv("PGHOST")
    PGPORT = getenv("PGPORT")
    PGUSER = getenv("PGUSER")
    PGDATABASE = getenv("PGDATABASE")
    PGPASSWORD = getenv("PGPASSWORD")


quote_channel_id = environ.get("QUOTE_CHANNEL_ID", 463657120441696256)
bot_token = environ.get("BOT_TOKEN")
