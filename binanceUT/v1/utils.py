from binance.client import Client
# import numpy as np
# from binance.enums import *
import finlab_crypto
# from finlab_crypto import Strategy
import pandas as pd
# from binance import Client
# import requests

# 建立客戶端
api_key = ''
api_secret = ''
client = Client(api_key=api_key,api_secret=api_secret)

def get_signal(
      pair='ETHUSDT',
      freq='15m',
      n_bar = 10000,
      client = client
      ):
    print('-----', client)
    ohlcv = finlab_crypto.crawler.get_nbars_binance(pair,freq,n_bar,client)
    close = ohlcv.close
    print(close)