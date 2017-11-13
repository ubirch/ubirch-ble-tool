from setuptools import setup, find_packages

config = {
	'description' : 'BLE wrapper around Mac-OS and Linux BLE libraries',
	'author' : 'Niranjan Rao',
	'url' : 'github.com/ubirch',
	'download_url' : 'github.com/ubirch/ubirch-ble-tool',
	'version' : '0.0.1',
	'license' : 'Apache License',
	'packages' : find_packages(),
	'scripts' : [],
	'name' : 'ubirch-ble-tool'
}

setup(**config)
