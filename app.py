from flask import Flask, request
import re
import numexpr
app = Flask(__name__)

def get_query_parameter(url):
    return url.split("calc?",1)[1]

@app.route('/')
def Homepage():
    return "Page Not Found"

@app.route("/calc")
def calc():

    url = request.url

    try:
        return str(numexpr.evaluate(get_query_parameter(url)))
    except KeyError:
        return "ERROR"

    return url

if __name__ == '__main__':
    app.run()
