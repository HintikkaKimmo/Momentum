import configparser
import oandapy
import pandas

# loading config variables from oanda.cfg file. Please see oanda_example.cfg.
config = configparser.ConfigParser()
config.read('oanda.cfg')

# Initializing Oanda API with config oath information
oanda = oandapy.API(environment='practice',
                    access_token=config['oanda']['access_token'])

# Loads Oanda trade history to data object with parameters below
data = oanda.get_history(instrument='EUR_USD', # instrument
                         start='2017-02-13',  # start date
                         end='2017-02-20',  # end date
                         granularity='M1')  # minute bars

# loads Oanda data to pandas DataFrame and sets time as index
df = pandas.DataFrame(data['candles']).set_index('time')




