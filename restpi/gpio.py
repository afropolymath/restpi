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
        try:
            self.config = self.setup(config)
        except Error:
            print "There was an error while trying to initialize GPIO"

    def setup(self, config):
        """
        Setup the board using the specified configuration parameters
        """
        GPIO.setmode(config['mode'])

        if 'mapping' in config:
            for i in config['mapping']['input']:
                GPIO.setup(channel, GPIO.IN)

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
