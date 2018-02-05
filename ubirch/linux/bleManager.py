from bleSuite import bleConnectionManager, bleServiceManager
from bluepy.btle import Scanner

from ubirch.linux.bleServiceManager import BLEServiceManager


class BLEManager(object):
    """ BLE network manager """

    def __init__(self, address, adapter, addressType, securityLevel, createRequester, psm=0, mtu=0):
        """ Create an instance of BLE Manager """
        self.address = address
        self.cm = bleConnectionManager.BLEConnectionManager(address, adapter, addressType, securityLevel)
        self.sm = BLEServiceManager(self.cm, self.address)

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
        # TODO add a function getHandlebyUUID toget handle using uuid
        # helps to read data on both mac n linux with ease
        return bleServiceManager.bleServiceReadByHandle(self.cm, handle)

    def isConnected(self):
        return self.cm.isConnected()


    # Services and Characteristics

    def bleServiceWriteToHandle(self, handle, data):
        return bleServiceManager.bleServiceWriteToHandle(self.cm, handle, data)

    def bleServiceReadByHandle(self, handle):
        return bleServiceManager.bleServiceReadByHandle(self.cm, handle)

    def bleServiceReadByUUID(self, uuid):
        return bleServiceManager.bleServiceReadByUUID(self.cm, uuid)

    def bleDiscoverServices(self):
        return bleServiceManager.bleServiceDiscovery(self.address, self.cm)

    def showServices(self):
        bledevice = bleServiceManager.bleServiceDiscovery(self.address, self.cm)
        bledevice.printDeviceStructure()

    def bleGetHandlefromUUID(self, uuid):
        bledevice = bleServiceManager.bleServiceDiscovery(self.address, self.cm)

        for service in bledevice.services:
            # print service.uuid
            for characteristic in service.characteristics:
                # print characteristic.uuid
                if uuid == characteristic.uuid:
                    return characteristic.valueHandle

        return -1


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
