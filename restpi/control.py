from flask import request
from flask_restful import Resource
from werkzeug.exceptions import BadRequest, InternalServerError

gpio = None

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO!  This is probably because you need " \
        "superuser privileges.  You can achieve this by using 'sudo' to run " \
        "your script"

class Channels(object):
    @staticmethod
    def initialize(api, config):
        """
        Initialize the API based on the config parameters
        """
        gpio = GpioControl(config)
        api.add_resource(ChannelListView, '/channels')
        api.add_resource(ChannelDetailView, '/channels/<int:channel_id>')
        return api

class ChannelListView(Resource):
    def get(self):
        """
        Returns a list of all the channels and their configuration
        """
        return gpio.config['mapping']

    def post(self):
        """
        Adds a new channel configuration or replaces one that already exists
        """
        try:
            channel_id = request.form['channel_id']
            mode = request.form['mode']

            if mode not in ['input', 'output']:
                raise BadRequest("The mode parameter is invalid")

            channel_id = int(channel_id)
            if channel_id not in gpio.config['mapping'][mode]:
                raise BadRequest("The channel_id parameter is invalid")

            gpio.set_mode(channel_id, mode)
        except:
            raise BadRequest("Error while parsing the channel_id parameters")


class ChannleDetailView(Resource):
    def get(self, channel_id):
        """
        Gets the channel status
        """
        if channel_id not in gpio.config['mapping'][mode]:
            raise BadRequest("The channel_id URL parameter is invalid")

        pin_status = gpio.read(channel_id)

        if pin_status is False:
            raise InternalServerError("Error occurred while trying to read" \
                "channel data")

        res = {
            "channel_id": channel_id,
            "pin_status": pin_status
        }

        return res

    def post(self, channel_id):
        """
        Updates channel status based on request
        """
        try:
            pin_status = int(request.form['pin_status'])
            if pin_status not in [0, 1]:
                raise BadRequest("The pin_status parameter is invalid")

            if not gpio.write(channel_id, pin_status):
                raise InternalServerError("The write process was not successful")

            res = {
                "channel_id": channel_id,
                "pin_status": pin_status
            }

            return res
        except Error:
            raise BadRequest("Error while parsing pin_status parameter")

class GpioControl(object):
    """
    Creates an object that abstracts away the logic of controlling the Pi using
    simpler and more elegant syntax.
    """
    def __init__(self, config):
        try:
            self.config = self.setup(config)
        except Error:
            print "There was an error while trying to initialize GPIO"

    def setup(self, config):
        """
        Setup the board using the specified configuration parameters
        """
        # Set board pin mapping mode from config
        GPIO.setmode(config['mode'])

        if 'mapping' in config:
            # Setup GPIO Input channels
            for i in config['mapping']['input']:
                GPIO.setup(channel, GPIO.IN)

            # Setup GPIO Output channels
            for i in config['mapping']['output']:
                GPIO.setup(channel, GPIO.OUT)

        return config

    def write(self, channel, data):
        """
        Write bit to a channel
        """
        if channel in self.config['mapping']['output']:
            try:
                GPIO.output(channel, data)
                return True
            except Error:
                return False
        return False

    def read(self, channel):
        """
        Read bit from a channel
        """
        if channel in config['mapping']['input']:
            try:
                return GPIO.input(channel)
            except Error:
                return False
        return False

    def set_mode(self, channel_id, mode):
        """
        Set the mode of a channel to the specified mode
        """
        rpi_mode = GPIO.OUT if mode == 'output' else GPIO.IN
        GPIO.setup(channel_id, rpi_mode)
        return True

    def end(self):
        """
        End the GPIO interaction session
        """
        GPIO.cleanup()
