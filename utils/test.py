import configparser

config = configparser.ConfigParser()
config.read('/Users/bosch/Desktop/PythonTestingFramework/features/properties.ini')
data=config['AndroidEmulator']['platformName']
print(data)
