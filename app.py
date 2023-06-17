import json
import urllib.request

from dotenv import dotenv_values
from flask import Flask, request

app = Flask(__name__)


# env constants
ENV = dotenv_values(".env")
ROOT_URL = ENV.get("ROOT_URL", "/")

# route constants
HOME_ROUTE_NAME = ""
BRUH_ROUTE_NAME = "bruh"
SHOOT_ROUTE_NAME = "shoot"
QUOTE_ROUTE_NAME = "quote"
HOME_ROUTE = "{root}{url}".format(url=HOME_ROUTE_NAME, root=ROOT_URL)
BRUH_ROUTE = "{root}{url}".format(url=BRUH_ROUTE_NAME, root=ROOT_URL)
SHOOT_ROUTE = "{root}{url}".format(url=SHOOT_ROUTE_NAME, root=ROOT_URL)
QUOTE_ROUTE = "{root}{url}".format(url=QUOTE_ROUTE_NAME, root=ROOT_URL)


@app.route(HOME_ROUTE)
def hello_world():
    return (
        "<main><p>Hello, World!</p>"
        "<section><a href={bruh_url}>{bruh_name}</a></section>"
        "<section><a href={shoot_url}?name=oic>{shoot_name}</a></section>"
        "<section><a href={quote_url}>{quote_name}</a></section>"
        "</main>".format(
            bruh_url=BRUH_ROUTE,
            bruh_name=BRUH_ROUTE_NAME,
            shoot_name=SHOOT_ROUTE_NAME,
            shoot_url=SHOOT_ROUTE,
            quote_url=QUOTE_ROUTE,
            quote_name=QUOTE_ROUTE_NAME,
        )
    )


@app.route(BRUH_ROUTE)
def oh():
    return {
        "oh": (
            "no--------- 00000000 0000000000"
            "0000000000 ooooooooooooooooooooooooooo"
            " oooooooooooooooooooooooo"
        )
    }


@app.route(SHOOT_ROUTE)
def shoot():
    name = request.args.get("name")
    return {
        "hai": (
            "u guyaii!! ____----{name}----____ fasdfasdfasdfasdf"
            " asdfasdfasdfasdfsdfasdfasdfasdfasdfasdf".format(name=name)
        )
    }


@app.route(QUOTE_ROUTE)
def quote():
    url = "https://catfact.ninja/fact"
    response = urllib.request.urlopen(url)
    data_response = response.read()
    data = json.loads(data_response)

    return data
