import configparser
import oandapy
import pandas

# loading config variables from oanda.cfg file. Please see oanda_example.cfg.
config = configparser.ConfigParser()
config.read('oanda.cfg')

# Initializing Oanda API with config oath information
oanda = oandapy.API(environment='practice',
                    access_token=config['oanda']['access_token'])




