from flask import Flask

app = Flask(__name__)

HOME_ROUTE_NAME = ""
BRUH_ROUTE_NAME = "bruh"
HOME_ROUTE = "/{url}".format(url=HOME_ROUTE_NAME)
BRUH_ROUTE = "/{url}".format(url=BRUH_ROUTE_NAME)


@app.route(HOME_ROUTE)
def hello_world():
    return "<main><p>Hello, World!</p><a href={url}>{name}</a></main>".format(
        url=BRUH_ROUTE, name=BRUH_ROUTE_NAME
    )


@app.route(BRUH_ROUTE)
def oh():
    return {"oh": "no"}
