from random import choice

from flask import Flask, render_template
from httpx import get
from psycopg2 import pool
from quoteswebsite.constants import PostgreSQL, bot_token, quote_channel_id

app = Flask(__name__)

connection_pool = pool.ThreadedConnectionPool(
    1,
    20,
    user=PostgreSQL.PGUSER,
    password=PostgreSQL.PGPASSWORD,
    host=PostgreSQL.PGHOST,
    port=PostgreSQL.PGPORT,
    database=PostgreSQL.PGDATABASE,
)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", authenticated=False)


@app.route("/api/quote", methods=["GET"])
def quote():
    connection = connection_pool.getconn()
    cursor = connection.cursor()
    cursor.execute("select quote_id from quotes;")
    records = cursor.fetchall()
    cursor.close()
    connection_pool.putconn(connection)
    message = get(
        f"https://discordapp.com/api/v7/channels/{quote_channel_id}/messages/{choice(records)[0]}",
        headers={"Authorization": f"Bot {bot_token}"},
    ).json()
    if message["embeds"] == []:
        return {
            "quote": message["content"],
            "author": message["author"]["username"],
            "id": message["id"],
        }
    else:
        return {
            "quote": message["embeds"][0]["description"],
            "author": message["embeds"][0]["author"]["name"],
            "id": message["id"],
        }


def main():
    app.run(host="0.0.0.0", port=80)
