from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    """Return simple "welcome" greeting. """

    return "welcome"

@app.route("/welcome/home")
def welcome_home():
    """Return simple "welcome home" greeting. """

    return "welcome home"

@app.route("/welcome/back")
def welcome_back():
    """Return simple "welcome back" greeting. """

    return "welcome back"