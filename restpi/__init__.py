from flask import Flask
from channel import ChannelControl

# TODO: Setup logging on the library and exception handling
# TODO: Ensure requests are non blocking and don't result in deadlocks
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

class RestServer(object):
    """
    Manages the server status and information. It also creates an instance of
    the Flask server used through out the application.
    """
    def __init__(self, module, config):
        self.app = Flask(module)
        api = Api(app)
        ChannelControl.initialize(api, config)

    def run(self, *args, **kwargs):
        """
        Wrapper for the Flask app run method
        """
        self.app.run(*args, **kwargs)
