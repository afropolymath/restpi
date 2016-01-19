from flask import Flask
from flask_restful import Resource
from control import GpioControl, Channels

import yaml

# TODO: Setup logging on the library and exception handling
# TODO: Ensure requests are non blocking and don't result in deadlocks
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO!  This is probably because you need " \
        "superuser privileges.  You can achieve this by using 'sudo' to run " \
        "your script"

class RestServer(object):
    """
    Manages the server status and information. It also creates an instance of
    the Flask server used through out the application.
    """
    def __init__(self, module, config_file):
        self.app = Flask(module)
        api = Api(app)

        # Create Flask application with default endpoints
        Channels.initialize(api, config_file)

        return self.app

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)
