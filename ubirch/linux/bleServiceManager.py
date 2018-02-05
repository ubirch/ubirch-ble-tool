from bleSuite import bleServiceManager


class BLEServiceManager(object):

    def __init__(self, connectionManager, address):
        self.connectionManager = connectionManager
        self.address = address

    def bleServiceWriteToHandle(self, handle, data):
        return bleServiceManager.bleServiceWriteToHandle(self.connectionManager, handle, data)

    def bleServiceReadByHandle(self, handle):
        return bleServiceManager.bleServiceReadByHandle(self.connectionManager, handle)

    def bleServiceReadByUUID(self, uuid):
        return bleServiceManager.bleServiceReadByUUID(self.connectionManager, uuid)

    def bleDiscoverServices(self):
        return bleServiceManager.bleServiceDiscovery(self.address, self.connectionManager)

    def showServices(self):
        bledevice = bleServiceManager.bleServiceDiscovery(self.address, self.connectionManager)
        bledevice.printDeviceStructure()
