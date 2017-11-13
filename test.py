import time

from  ubirch.ble_platform import get_manager, get_scanner
# from bleManager import BLEManager, BLEScanDevices

scandevices = get_scanner()

def setup():
    print "SETUP!!"

def tear_down():
    print "TEAR DOWN.."

def test_basic():
    print "Test Basic"
    mydev = scandevices.getDeviceAddress("TRACK", 5)
    print mydev
    return mydev

address = test_basic()
adapter = ""
addressType = "random"
securityLevel = "low"
handle =  0x10 #int("6c", 16)
uuid = "6e400003-b5a3-f393-e0a9-e50e24dcca9e"
createRequester = False

ignoreUUID = ["00001800-0000-1000-8000-00805f9b34fb", "00001801-0000-1000-8000-00805f9b34fb"]

cm = get_manager(address, adapter, addressType, securityLevel, createRequester)
cm.connectDevice()
chars = cm.discoverCharacteristics()
for i in chars:
    print "char : ", i

data = cm.read(handle)
time.sleep(0.5)
data1 = cm.read(handle)
print "Data :", data
print "Data1:", data1

# TODO Find a way to clear the read buffer
data1 = data1[0][len(data[0]):]
print "new Data1:", data1

cm.write(0xe, "uuid\r\n")
cm.disconnectDevice()