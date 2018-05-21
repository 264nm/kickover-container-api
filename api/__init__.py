#!/usr/bin/env python2
from flask import Flask

from auth import *
from config import *


#def create_app():
#    api_version = 'v1'
#    route_base = '/api/' + api_version
#    ContainerView.register(app, route_base=route_base + '/container')
#    app.config.from_object(config.DevelopmentConfig)
##    app.logger.setLevel(logging.ERROR)
#    return app
