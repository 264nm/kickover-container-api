#!/usr/bin/env python2
import sys
import os
import time
import signal
from threading import Thread
from flask import Flask
from flask import jsonify
from flask_api import status
from flask_classy import FlaskView, route
from flask import current_app as app
from auth import *

def _restart_container(app):
    time.sleep(5)
    try:
        os.kill(1, signal.SIGTERM)
    except OSError as e:
        app.logger.error("You need root permissions to kill PID 1")
        sys.exit(1)

class ContainerView(FlaskView):
    @route('/restart')
    @requires_auth
    def simulate_restart(self):
        result = { 'message' : 'Restart request received. Attempting to kill PID 1 in 5s' }
        if os.geteuid() == 0:
            status_code = 200
        else:
            app.logger.warning('Restart request to kill PID 1 requires root permissions. Current UID: ' + str(os.geteuid()))
            result['message'] = 'Restart request received but process is not running as root'
            status_code = 403

        thread = Thread(target=_restart_container,kwargs={'app': app._get_current_object()})
        thread.start()
        return (jsonify(result), status_code)


