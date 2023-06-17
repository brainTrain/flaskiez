from flask import Flask, request

app = Flask(__name__)

HOME_ROUTE_NAME = ""
BRUH_ROUTE_NAME = "bruh"
SHOOT_ROUTE_NAME = "shoot"
HOME_ROUTE = "/{url}".format(url=HOME_ROUTE_NAME)
BRUH_ROUTE = "/{url}".format(url=BRUH_ROUTE_NAME)
SHOOT_ROUTE = "/{url}".format(url=SHOOT_ROUTE_NAME)


@app.route(HOME_ROUTE)
def hello_world():
    return (
        "<main><p>Hello, World!</p> <section><a"
        " href={bruh_url}>{bruh_name}</a></section> <section><a"
        " href={shoot_url}?name=oic>{shoot_name}</a></section> </main>".format(
            bruh_url=BRUH_ROUTE,
            bruh_name=BRUH_ROUTE_NAME,
            shoot_name=SHOOT_ROUTE_NAME,
            shoot_url=SHOOT_ROUTE,
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
