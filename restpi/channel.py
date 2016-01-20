from flask import request
from flask_restful import Resource
from gpio import GpioControl
from werkzeug.exceptions import BadRequest, InternalServerError

gpio = None

class ChannelControl(object):
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
