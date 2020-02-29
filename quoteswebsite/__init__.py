from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html", authenticated=False)

def main():
    app.run(host="0.0.0.0", debug=True)
