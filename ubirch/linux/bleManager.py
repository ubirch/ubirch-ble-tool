from bleSuite import bleConnectionManager, bleServiceManager
from bluepy.btle import Scanner


class BLEManager(object):
    """ BLE network manager """

    def __init__(self, address, adapter, addressType, securityLevel, createRequester, psm=0, mtu=0):
        """ Create an instance of BLE Manager """
        self.address = address
        self.cm = bleConnectionManager.BLEConnectionManager(address, adapter, addressType, securityLevel)

    def connectDevice(self):
        """ conect tot he BLE device
            take manager object or mac address as a input variable
        """
        self.cm.connect()

    def disconnectDevice(self):
        self.cm.disconnect()

    def discoverDevice(self, name, timeout=5):
        sm = BLEScanDevices()
        deviceList = sm.scan(timeout)
        for device in deviceList:
            for values in device.getScanData():
                if values[2].rstrip('\x00') == name:
                    return str(device.addr)
        raise Exception("NO DEVICE FOUND")

    def discoverServices(self):
        return bleServiceManager.bleServiceDiscovery(self.address, self.cm)

    def discoverCharacteristics(self):
        ignoreUUID = ["00001800-0000-1000-8000-00805f9b34fb", "00001801-0000-1000-8000-00805f9b34fb"]
        devServices = self.discoverServices()
        devCharList = []
        for service in devServices.services:
            if not (service.uuid in ignoreUUID):
                for characteristics in service.characteristics:
                    devCharList.append(characteristics.uuid)
                return devCharList
        raise Exception("No Services Found")


    def write(self, handle, data):
        bleServiceManager.bleServiceWriteToHandle(self.cm, handle, data)

    def read(self, handle):
        return bleServiceManager.bleServiceReadByHandle(self.cm, handle)

    def isConnected(self):
        return self.cm.isConnected()


class BLEScanDevices(object):

    def __init__(self):
        self.sm = Scanner()

    def scan(self, timeOut=10):
        return self.sm.scan(timeOut)

    def stopScan(self):
        pass

    def isScanning(self):
        pass

    def getDeviceAddress(self, deviceName, timeOut=10):
        """return a tuple containing DeviceName and DeiceAddress"""
        deviceList = self.scan(timeOut)
        for device in deviceList:
            for values in device.getScanData():
                if values[2].rstrip('\x00') == deviceName:
                    return str(device.addr)
        raise Exception("NO DEVICE FOUND")
