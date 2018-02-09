# Python BLE wrapper 

A wrapper around the OSX and Linux Python BLE Libraries to simplify access to BLE devices on OSX and Linux
 
```
Note: - Just the basic functions like Scan, Connect, Discover Services, Read/ Write to handle
        are implemented
      - Mac-OSX support is yet to be tested
```

## Supported Platforms

The wrapper supports the following platforms:

* Linux, using [bluepy](https://github.com/IanHarvey/bluepy), [Gattlib](https://pypi.python.org/pypi/gattlib/0.20150805) and [BLESuite](https://github.com/nccgroup/BLESuite) libraries
* Mac OSX, using [PyBLEWrapper](https://github.com/brettchien/PyBLEWrapper) library 


## Linux

- Install the latest version of [BlueZ](https://docs.ubuntu.com/core/en/stacks/bluetooth/bluez/docs/install-bluez)
- Clone the [ubirch-ble-tool](git@github.com:ubirch/ubirch-ble-tool.git)

 > run  `pip install -r requirements.txt` to install the required libraries
run `python setup.py install` to install ``ubirch-ble-tool``



## Mac-OSX
- Clone the [ubirch-ble-tool](git@github.com:ubirch/ubirch-ble-tool.git)

 > run `pip install -U git+https://github.com/brettchien/PyBLEWrapper.git` to install the [PyBLEWrapper](https://github.com/brettchien/PyBLEWrapper),   
run `python setup.py install` to install ``ubirch-ble-tool``
