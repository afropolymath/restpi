import unittest
from restpi import RestServer


class TestChannel(unittest.TestCase):
    def setup(self):
        self.restserver= RestServer
        self.api = Api(Flask(__name__))
        self.config = {
            'mode': 'BOARD',
            'mapping': {
                'input': [],
                'output': []
            }
        }

    def test_channel_initialize(self):
        api = ChannelControl.initialize(self.api, config)
        self.assertIsInstance(api, Api)
