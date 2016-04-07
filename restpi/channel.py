from flask import request
from flask_restful import Resource
from gpio import GpioControl
from werkzeug.exceptions import BadRequest, InternalServerError


class ChannelControl(object):
    gpio_obj = None

    @classmethod
    def initialize(cls, api, config):
        """
        Initialize the API based on the config parameters
        """
        cls.gpio_obj = GpioControl.setup(config)
        api.add_resource(ChannelListView, '/channels')
        api.add_resource(ChannelDetailView, '/channels/<int:channel_id>')
        return api


class ChannelListView(Resource):
    def get(self):
        """
        Returns a list of all the channels and their configuration
        """
        return ChannelControl.gpio_obj.config['mapping']

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
            if channel_id not in ChannelControl.gpio_obj.config['mapping'][mode]:
                raise BadRequest("The channel_id parameter is invalid")

            ChannelControl.gpio_obj.set_mode(channel_id, mode)
        except:
            raise BadRequest("Error while parsing the channel_id parameters")


class ChannelDetailView(Resource):
    def get(self, channel_id):
        """
        Gets the channel status
        """
        try:
            channel_id = int(channel_id)
        except Exception:
            raise InternalServerError(
                "Invalid channel_id parameter"
            )
        pin_status = ChannelControl.gpio_obj.read(channel_id)

        if pin_status is False:
            raise InternalServerError(
                "Error occurred while trying to read channel data"
            )

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
            pin_status = int(request.json['pin_status'])
            if pin_status not in [0, 1]:
                raise BadRequest("The pin_status parameter is invalid")

            if not ChannelControl.gpio_obj.write(channel_id, pin_status):
                raise InternalServerError(
                    "The write process was not successful"
                )

            res = {
                "channel_id": channel_id,
                "pin_status": pin_status
            }

            return res
        except Error:
            raise BadRequest("Error while parsing pin_status parameter")
