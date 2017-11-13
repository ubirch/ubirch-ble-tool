# Python BLE wrapper 

A wrapper around the OSX and Linux Python BLE Libraries to simplify access to BLE devices on OSX and Linux
 
```
Note: - Just the basic functions like Scan, Connect, Discover Services, Read/ Write to handle
        are implemented
      - Mac-OSX support is yet to be tested
```

## Supported Platforms

The wrapper supports the following platforms:

* Linux, using [bluepy](https://github.com/IanHarvey/bluepy) and [BLESuite](https://github.com/nccgroup/BLESuite) libraries
* Mac OSX, using [PyBLEWrapper](https://github.com/brettchien/PyBLEWrapper) library 


## Linux

On Linux you'll need to compile and install the latest version of BlueZ, currently version 5.33,
to gain access to the Bluetooth LE API it exposes and also install [bluepy](https://github.com/IanHarvey/bluepy) and [BLESuite](https://github.com/nccgroup/BLESuite)

run `python setup.py install` to install ``ubirch-ble-tool``
## Mac-OSX

Install the [PyBLEWrapper](https://github.com/brettchien/PyBLEWrapper)
```
pip install -U git+https://github.com/brettchien/PyBLEWrapper.git
```

## Installing

To install `ubirch-ble-tool run` ```pip install -U git+https://github.com/ubirch/ubirch-ble-tool.git```

# License

This wrapper is available under the [Apache License](LICENSE)

```
Copyright 2017 ubirch GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
````
