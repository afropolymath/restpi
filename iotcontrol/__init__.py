from flask import Flask
from control import ChannelOperations

import yaml

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}

# TODO: Setup logging on the library and exception handling
# TODO: Ensure requests are non blocking and don't result in deadlocks
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO!  This is probably because you need " \
        "superuser privileges.  You can achieve this by using 'sudo' to run " \
        "your script"

class IOTServer(object):
    """
    Manages the server status and information. It also creates an instance of
    the Flask server used through out the application.
    """
    def __init__(self, module, config=None):
        # Create GPIO interface
        self.gpio = GPIOControl(config)

        # Create Flask application with default endpoints
        self.app = self.__maproutes__(Flask(module))

    def __maproutes__(self, app):
        """
        Define initial default endpoints for the application
        """
        app.add_url_rule('/channels', view_func=ChannelOperations.list)
        app.add_url_rule('/channels/<channel_id>', view_func=ChannelOperations.detail,  methods= ['GET', 'POST'])
        return app

class GPIOControl(object):
    """
    Creates an object that abstracts away the logic of controlling the Pi using
    simpler and more elegant syntax.
    """
    def __init__(self, config):
        if config is not None
            config = self.parseconfig(config)

        self.setup(config)

    def parseconfig(self, config_file):
        """
        Parse configuration details from YAML file to dictionary
        """
        try:
            with open(config_file) as stream:
                config = yaml.load(stream)
                return config
        except Error:
            raise "Could not parse the configuration file"

    def setup(self, config=None):
        """
        Setup the board using the specified configuration parameters
        """
        if config is None:
            # Set basic configuration parameters
            config = {
                mode: 'BOARD'
            }

        # Set board pin mapping mode from config
        GPIO.setmode(config['mode'])

        if 'mapping' in config:
            # Setup GPIO Input channels
            for i in config['mapping']['input']:
                GPIO.setup(channel, GPIO.IN)

            # Setup GPIO Output channels
            for i in config['mapping']['output']:
                GPIO.setup(channel, GPIO.OUT)

        # Store configuration parameters
        self.config = config

    def write(self, channel, data):
        """
        Write bit to a channel
        """
        if channel in config['mapping']['output']:
            GPIO.output(channel, data)
            return True
        return False

    def read(self, channel):
        """
        Read bit from a channel
        """
        if channel in config['mapping']['input']:
            GPIO.input(channel)
            return True
        return False

    def end(self):
        GPIO.cleanup()
