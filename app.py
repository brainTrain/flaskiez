import json

import requests
from dotenv import dotenv_values
from flask import Flask, render_template, request

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
def home():
    return render_template(
        "index.html",
        bruh_url=BRUH_ROUTE,
        bruh_name=BRUH_ROUTE_NAME,
        shoot_name=SHOOT_ROUTE_NAME,
        shoot_url=SHOOT_ROUTE,
        quote_url=QUOTE_ROUTE,
        quote_name=QUOTE_ROUTE_NAME,
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
    data_1 = get_cat_facts()
    data_2 = get_dad_joke()

    return {"data 1": data_1, "data 2": data_2}


def get_cat_facts():
    url = "https://catfact.ninja/fact"
    response = requests.get(url)

    data_response = response.text
    data = json.loads(data_response)

    return data


def get_dad_joke():
    url = "https://icanhazdadjoke.com/"
    response = requests.get(url, headers={"Accept": "application/json"})
    data_response = response.text
    data = json.loads(data_response)

    return data
