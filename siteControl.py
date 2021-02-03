from flask import Flask
app = Flask(__name__)
@app.route("/")
def helloWorld():
    return "dolla dolla bills yo"

@app.route("/someOtherPage")
def someOtherPage():
    return "WOW TWO PAGES"