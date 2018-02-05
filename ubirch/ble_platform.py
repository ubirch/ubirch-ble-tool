import sys


# Keep a single global instance of the BLE provider.
_manager = None
_scanner = None
_service_manager = None

def get_manager(address, adapter, addressType, securityLevel, createRequester, psm=0, mtu=0):
    """Return an instance of the BLE provider for the current platform."""
    global _manager
    # Set the provider based on the current platform.
    if _manager is None:
        if sys.platform.startswith('linux'):
            # Linux platform
            from linux.bleManager import BLEManager
            from linux.bleServiceManager import BLEServiceManager
            _manager = BLEManager(address, adapter, addressType, securityLevel, createRequester, psm, mtu)
        elif sys.platform == 'darwin':
            pass
            # Mac OSX platform
            from macos.bleManager import BLEManager
            _manager = BLEManager(address, adapter, addressType, securityLevel, createRequester, psm, mtu)
        else:
            # Unsupported platform
            raise RuntimeError('Sorry the {0} platform is not supported by the BLE library!'.format(sys.platform))
    return _manager

def get_scanner():
    """Return an instance of the BLE provider for the current platform."""
    global _scanner
    # Set the provider based on the current platform.
    if _scanner is None:
        if sys.platform.startswith('linux'):
            # Linux
            from linux.bleManager import BLEScanDevices
            _scanner = BLEScanDevices()
        elif sys.platform == 'darwin':
            pass
            # Mac OSX platform
            from macos.bleManager import BLEScanDevices
            _scanner = BLEScanDevices()
        else:
            # Unsupported platform
            raise RuntimeError('Sorry the {0} platform is not supported by the BLE library!'.format(sys.platform))
    return _scanner

def get_service_manager():
    """Return an instance of the BLE provider for the current platform."""
    global _service_manager
    # Set the provider based on the current platform.
    if _service_manager is None:
        if sys.platform.startswith('linux'):
            # Linux platform
            from linux.bleServiceManager import BLEServiceManager
            _service_manager = BLEServiceManager()
        elif sys.platform == 'darwin':
            pass
            # Mac OSX platform
        else:
            # Unsupported platform
            raise RuntimeError('Sorry the {0} platform is not supported by the BLE library!'.format(sys.platform))
    return _service_manager
