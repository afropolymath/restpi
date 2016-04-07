from flask import Flask
from flask_restful import Api
from channel import ChannelControl

# TODO: Setup logging on the library and exception handling
# TODO: Ensure requests are non blocking and don't result in deadlocks
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)


class RestServer(object):
    """
    Manages the server status and information. It also creates an instance of
    the Flask server used through out the application.
    """
    def __init__(self, config):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api = ChannelControl.initialize(self.api, config)

    def run(self, *args, **kwargs):
        """
        Wrapper for the Flask app run method
        """
        print "Now running REST-Pi Server..."
        self.app.run(*args, **kwargs)
