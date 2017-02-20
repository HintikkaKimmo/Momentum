import configparser
import oandapy
import pandas

config = configparser.ConfigParser()
config.read('oanda.cfg')

oanda = oandapy.API(environment='practice',
                    access_token=config['oanda']['access_token'])


