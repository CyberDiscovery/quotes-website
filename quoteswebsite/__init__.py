from flask import Flask, render_template, redirect, request
from os import environ
import psycopg2
import psycopg2
from psycopg2 import pool
from quoteswebsite.constants import PostgreSQL

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
    cursor.execute("select quote_id from quotes")
    records = cursor.fetchall()
    cursor.close()
    connection_pool.putconn(connection)
    return records



def main():
    app.run(host="0.0.0.0")
