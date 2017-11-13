from pyble import CentralManager
from pyble.handlers import PeripheralHandler, DefaultProfileHandler

class BLEManager(object):
    """ BLE network manager """

    def __init__(self, address, adapter, addressType, securityLevel, createRequester, psm=0, mtu=0):
        """ Create an instance of BLE Manager """
        self.address = address
        self.cm = CentralManager()

    def connectDevice(self):
        """ conect tot he BLE device
            take manager object or mac address as a input variable
        """
        self.address.delegate = Peripheral
        self.peripheral = self.cm.connectPeripheral(self.address)

    def disconnectDevice(self):
        self.cm.disconnectPeripheral(self.peripheral)

    def discoverDevice(self, name, timeout=10):
        self.cm.startScan(timeout)
        for target in self.cm.scanedList:
            if target and target.name == name:
                return target
            else:
                raise Exception("Device not found")
        raise Exception("No DeviceFound")

    def discoverServices(self):
        return self.peripheral

    def discoverCharacteristics(self):
        ignoreUUID = ["00001800-0000-1000-8000-00805f9b34fb", "00001801-0000-1000-8000-00805f9b34fb"]
        devCharList = []
        for service in self.peripheral:
            if not (service.uuid in ignoreUUID):
                for characteristics in service:
                    devCharList.append(characteristics)
                return devCharList
        raise Exception("No Services Found")

    def write(self, handle, data):
        c = self.peripheral["UART Profile"]["UART TX"]
        c.value = bytearray(data)

    def read(self, handle):
        c = self.peripheral["UART Profile"]["UART RX"]
        c.notify = True
        #TODO read values with and with notify
        return c.value

    def isConnected(self):
        pass


class BLEScanDevices(object):
    def __init__(self):
        self.cm = CentralManager()

    def scan(self, timeout=10):
        return self.cm.startScan(timeout)

    def stopScan(self):
        pass

    def isScanning(self):
        pass

    def getDeviceAddress(self, deviceName, timeOut=10):
        for target in self.cm.scanedList:
            if target and target.name == deviceName:
                return target
            else:
                raise Exception("Device not found")
        raise Exception("No DeviceFound")


class GenericProfileHandler(DefaultProfileHandler):
    UUID = "6E400001-B5A3-F393-E0A9-E50E24DCCA9E"
    _AUTOLOAD = True
    names = {
        "6E400001-B5A3-F393-E0A9-E50E24DCCA9E": "UART Profile",
        "6E400002-B5A3-F393-E0A9-E50E24DCCA9E": "UART TX",
        "6E400003-B5A3-F393-E0A9-E50E24DCCA9E": "UART RX"
    }

    def initialize(self):
        print "init"
        pass

    def on_write(self, characteristic, data):
        print "** write(" + str(characteristic.UUID) + "): '"+("".join(data))+"'"


    def on_read(self, characteristic, data):
        print "** read(" + str(characteristic.UUID) + "): '"+("".join(data))+"'"

    def on_notify(self, characteristic, data):
        print "** notify(" + str(characteristic.UUID) + "): '"+("".join(data))+"'"


class Peripheral(PeripheralHandler):
    def initialize(self):
        self.addProfileHandler(GenericProfileHandler)
        pass

    def on_connect(self):
        print "** connect(", self.peripheral, ")"
        pass

    def on_disconnect(self):
        print "** disconnect(", self.peripheral, ")"
        pass

    def on_rssi(self, value):
        print "** updateRSSI(", self.peripheral, ",", value, ")"
        pass
