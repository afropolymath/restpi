from flask import Flask
app = Flask(__name__)

# Installable via PIP and can be run with default configuration
# Make ngrok a dependency
# Create PubNub channel and then use channel id with Public API on platform
# pip install iotcontrol
# iotcontrol run - Runs default setup, server and the endpoints
# iotcontrol serve --port=xx --host=xx

# Think about possibility of using PubNub workflow or ngrok workflow
# Using ngrok you want the app to automatically generate a URL for you

# Can import it into app, create a new instance and run the Flask engine with the default endpoints directly from your app
# from iot-ontrol import IOTServer
# app = IOTServer(__name__)
# app.config(pin_mapping as an object)
# Exceptions everywhere
# app.set(PIN, status)
# if __name__ == '__main__':
#   app.start()
# From your app you can set further configuration like accessibility for pins and useful documentation for mapping

# Research into connecting to sensors to get status of sensors (v2)

# Returns some report of the pins structure on the Pi (Connected PINS, Devices connected, Documentation) - Need to figure out workflow
# For each individual PIN can get status and/or set the value to high or low
# Toggle functionality for each PIN
