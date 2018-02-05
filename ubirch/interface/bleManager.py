class BLEManager(object):
    """ BLE network manager """

    def __init__(self, address, adapter, addressType, securityLevel, createRequester, psm=0, mtu=0):
        pass

    def connectDevice(self):
        pass

    def disconnectDevice(self):
        pass

    def discoverDevice(self, name, timeout=5):
        pass

    def discoverServices(self):
        pass

    def discoverCharacteristics(self):
        pass

    def write(self, handle, data):
        pass

    def read(self, handle):
        pass

    def isConnected(self):
        pass
