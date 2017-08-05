import logging
from operator import itemgetter

import requests
from flask import Flask
from flask_ask import Ask, statement


app = Flask(__name__)
ask = Ask(app, '/')
logger = logging.getLogger()


@ask.launch
def launch():
    return doSomething()


@ask.intent("StatsIntent")
def doSomething():
    return { "hello": "world"}