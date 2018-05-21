#!/usr/bin/env python2
import os

class BaseConfig(object):
    """Base configuration"""
    DEBUG = False
    TESTING = False
    BASIC_AUTH_USERNAME = os.environ.get('CONTAINER_API_AUTH_USERNAME', 'admin')
    BASIC_AUTH_PASSWORD = os.environ.get('CONTAINER_API_AUTH_PASSWORD', 'pass123')
    BASIC_AUTH_FORCE = True
    SERVER_NAME = "%s:%s" % (os.environ.get('CONTAINER_API_SERVER', '0.0.0.0'),os.environ.get('CONTAINER_API_PORT', 5000))
class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    DEBUG = True
class TestingConfig(BaseConfig):
    """Testing configuration"""
    DEBUG = True
    TESTING = True
class ProductionConfig(BaseConfig):
    """Production configuration"""
    DEBUG = False
