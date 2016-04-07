try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print "Error importing RPi.GPIO!  This is probably because you need " \
        "superuser privileges.  You can achieve this by using 'sudo' to run " \
        "your script"

class GpioControl(object):
    """
    Creates an object that abstracts away the logic of controlling the Pi using
    simpler and more elegant syntax.
    """
    def __init__(self, config):
        self.config = config

    @staticmethod
    def setup(config):
        """
        Setup the board using the specified configuration parameters
        """
        GPIO.setmode(config['mode'])

        if 'mapping' in config:
            for channel in config['mapping']['input']:
                GPIO.setup(channel, GPIO.IN)
            for channel in config['mapping']['output']:
                GPIO.setup(channel, GPIO.OUT)

        print GPIO.mapping
        return GpioControl(config)

    def write(self, channel, data):
        """
        Write bit to a channel
        """
        if channel in self.config['mapping']['output']:
            try:
                GPIO.output(channel, data)
                return True
            except Exception:
                return False
        return False

    def read(self, channel):
        """
        Read bit from a channel
        """
        if channel in self.config['mapping']['input']:
            try:
                return GPIO.input(channel)
            except Exception:
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
