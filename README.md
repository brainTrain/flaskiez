# flaskiez
playin around with flasssssssk

## Setting up
* create virtual env
  * `python3 -m venv env`
* activate virtual env
  * `source env/bin/activate`
  * can now type `python` instead of `python3`
* deactivate virtual env
  * `deactivate`
* install dependencies
  * `pip install -r requirements.txt`
* install pre-commit hooks
  * `pre-commit install`
    * make sure your venv is activated when you run this

## Run
* `flask --app app run --debug`

## Troubleshooting

### Access Denied fro running flask server
* try `chrome://net-internals/#sockets` to clear local browser data for that url
  * [source](https://www.reddit.com/r/flask/comments/ttawkw/comment/iqrz3jw/)

## Pre commit stuffs
* install pre-commit hooks
  * `pre-commit install`
    * make sure your venv is activated when you run this
  * do this every time you update the `.pre-commit-config.yaml` file

## Tools

### pre-commit
  * gives yaml configurable pre-commit hook to add processers/parsers on commit
  * [GitHub](https://github.com/pre-commit/pre-commit#pre-commit)

### Black
  * code formatter based on PEP8 rules
  * [GitHub](https://github.com/psf/black#the-uncompromising-code-formatter)

### isort
  * code formatter that sorts imports based on PEP8 rules
  * [GitHub](HTTPS://GITHUB.COM/PYCQA/ISORT)

### Flake8
  * linter
  * [GitHub](https://github.com/pycqa/flake8#flake8)

### mypy
  * static typing
  * [GitHub](https://github.com/python/mypy#mypy-static-typing-for-python)
