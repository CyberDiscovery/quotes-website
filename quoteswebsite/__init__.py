from flask import Flask, render_template, redirect, request
from flask_discord import DiscordOAuth2Session
from functools import wraps
import configparser
import json

config = configparser.ConfigParser()
config.read("config.ini")


app = Flask(__name__)
app.secret_key = config["app"]["secret_key"]

app.config["DISCORD_CLIENT_ID"] = config["discord_oauth"]["ID"]
app.config["DISCORD_CLIENT_SECRET"] = config["discord_oauth"]["secret"]
app.config["DISCORD_REDIRECT_URI"] = config["discord_oauth"]["redirectURI"]
discord = DiscordOAuth2Session(app)

def validUser():
    if discord.authorized:
        inServer = False
        guilds = discord.get("/users/@me/guilds")
        for guild in guilds:
            # print(dir(guild))
            # print(guild["id"], config["discord_oauth"]["serverID"])
            if guild["id"] == str(config["discord_oauth"]["serverID"]):
                inServer = True
        return inServer
    else:
        return False


def sign_in_required(route):
    @wraps(route)
    def wrapper(*args, **kwargs):
        if validUser():
            return route(*args, **kwargs)
        else:
            return redirect("/login")
    return wrapper

@app.route("/", methods=["GET"])
@sign_in_required
def index():
    return render_template("index.html", authenticated=False)

@app.route("/login", methods=["GET"])
def login():
    if validUser():
        return redirect("/")
    else:
        return render_template("login.html")

@app.route("/oauth_redir", methods=["GET"])
def oauthRedirect():
    return discord.create_session("identify guilds")

@app.route("/oauth_callback", methods=["GET"])
def oauthCallback():
    discord.callback()
    return redirect("/")

def main():
    app.run(host="0.0.0.0", debug=True)
