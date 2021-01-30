from flask import *
from markupsafe import escape

app = Flask(__name__)
@app.route("/")
def helloWorld():
    return "dolla"

@app.route("/someOtherPage")
def someOtherPage():
    return "WOW TWO PAGES"

@app.route("/user/<username>")
def profile(username):
    return "{}'s profile".format(escape(username))

with app.test_request_context():
    print(url_for("helloWorld"))
    print(url_for("someOtherPage"))
    print(url_for("profile", username="whatever"))