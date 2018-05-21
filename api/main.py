#!/usr/bin/env python2
from flask import Flask
from flask_api import status
from flask_classy import FlaskView, route
from flask_basicauth import BasicAuth
from views.restart import ContainerView
import config
from auth import *
from views import *
app = Flask(__name__)

def create_app():
     __api_version__ = 'v1'
     route_base = '/api/' + __api_version__
     ContainerView.register(app, route_base=route_base + '/container')
     app.config.from_object(config.DevelopmentConfig)
     return app


if __name__ == '__main__':
     create_app()
     app.run(threaded=True)
