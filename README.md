# REST-Pi

Nifty Library written in Python for controlling Raspberry Pi based devices remotely.

### Requirements

[ngrok](https://ngrok.com/) is required to enable REST-Pi create a publicly accessible URL for your device.

### Installation

To use the library you need to install it on your Raspberry Pi. Ensure that Python is installed on your Pi (recommended version is 2.7.XX). The library is available on [PyPi](https://pypi.python.org/pypi), the Python Package Index and is installable via the `pip` command. Simply run:

```sh
$ pip install restpi
```

### Usage

To activate the REST-Pi server, simply run:

```sh
$ restpi serve --config=<PATH_TO_CONFIG_FILE> [--port=<PORT_NUMBER>]
```

- `PORT_NUMBER` (optional) - The port via which you want to allow remote accesses to your device.
- `PATH_TO_CONFIG_FILE` - The path to the config file that will be used to setup the board.

The library will automatically create a publicly accessible API which you may use to control your device via any programming language, application or even POSTMAN. The library will also display a randomly generated API Key which you will need to authenticate your requests. The key by default is set not to expire for the lifetime of the server.

### Default API Access Endpoints

The default API structure looks like this

| EndPoint  | Method | Description |
| ------------- | ------------- | ------------- |
| `/channels`  | GET  | Get full list of all the available pins and their statuses. |
| `/channels`  | POST  | Update a pin's configuration. The request JSON should be in the following format: `{ 'channel_id': XX, 'mode': 'input' }` where `mode` can either be 'input' or 'output' corresponding to the mode you would like to set for that `channel_id`. |
| `/channels/:channel_id`  | GET  | Get pin status of an input pin with id `channel_id`. |
| `/channels/:channel_id`  | POST  | Update the status of an output pin with id `channel_id`. The request JSON should be in the following format: `{ 'channel_id': XX, 'pin_status': 0 }` where `pin_status` can either be 0 or 1 corresponding to OFF or ON states. |

### Configuration and Modes

The configuration information used with the library is stored in a `.yml` file. This file will contain information to help setup your board for remote access. The format allows you to adequately document what each pin's mode is.

Sample format for the `.yml` is shown below:

```yaml
mode: BOARD
mapping:
  input:
    - 1
    - 2
    - 3
  output:
    - 4
    - 5
    - 6
```

The main configuration parameters to take not of are the `mode` and the `mapping`.

The `mode` parameter can be one of `BOARD` or `BCM` corresponding to the pin mapping mode we would like to make use of. See here for information on this.

The `mapping` parameter has two sub-keys which are `input` and `output`. These specify the channels we would like to provision as input and output channels respectively. Before the server is started, this information is used to setup the respective channels. A channel can only be setup for one mode at a time and so channels duplicated as input and output will be made to use the first selected mode.

You are allowed to only specify one of either the `input` or `output` parameters in the yaml file.
