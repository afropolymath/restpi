# REST-Pi
Nifty Library written in Python for controlling Raspberry Pi based devices remotely.

## Requirements
[ngrok](https://ngrok.com/) is required to enable REST-Pi create a publicly accessible URL for your device.

## Installation
To use the library you need to install it on your Raspberry Pi. Ensure that Python is installed on your Pi (recommended version is > 2.7.10). The libary is available on [PyPi](https://pypi.python.org/pypi), the Python Package Index and is installable via the `pip` command. Simply run:
```
pip install iotcontrol
```
## Usage
The default use case of the library is via the command line using the barest minimum settings, making all your GPio pins accessible remotely. **This is not recommended and should not be used except for when being used in sandbox mode**. To activate the REST-Pi server in this mode, simply run:
```
restpi serve <PORT_NUMBER>
```
- `PORT_NUMBER` - The port via which you want to allow remote accesses to your device.

The library will automatically create a publicly accessible API which you may use to control your device via any programming language, application or even POSTMAN. The libary will also display a randomly generated API Key which you will need to authenticate your requests. The key by default is set not to expire for the lifetime of the server.

## Configuration and Modes
Using the Library in the default mode as mentioned earlier is not recommended. The ideal way of using the libary is using it along with a `.yml` configuration file. This file will overwrite default configuration with those specified. The format allows you to adequately document the function of your device and each pin. This is of course applicable if you would like to create a more interactive experience when accessing your device. Advanced features such as pin level access is also configurable via the file. See here for more information on the file format and specifications.

## Default API Access Endpoints
The default API structure looks like this

| EndPoint  | Method | Description |
| ------------- | ------------- | ------------- |
| `/channels`  | GET  | Get full list of all the available pins and their statuses |
| `/channels`  | POST  | Update multiple pins at a time based on the signature in the JSON data passed |
| `/channels/:channel_id`  | GET  | Get pin status of pin with id `channel_id` |
| `/channels/:channel_id/:status`  | GET  | Update the status of pin with id `channel_id`. The status can either be 0 or 1 corresponding to OFF or ON |
