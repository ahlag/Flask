from flask import Flask, request
import re
import numexpr
app = Flask(__name__)

def validate_url(url):
    regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None

def get_query_parameter(url):
    return url.split("calc?",1)[1]

@app.route('/')
def Homepage():
    return "Page Not Found"

@app.route("/calc")
def calc():


    url = request.url

    if validate_url(url) is False:
        return "ERROR"

    try:
        return str(numexpr.evaluate(get_query_parameter(url)))
    except KeyError:
        return "ERROR"

    return url

if __name__ == '__main__':
    app.run()
