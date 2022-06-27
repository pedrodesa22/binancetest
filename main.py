import pandas as pd
# import os

from binance import Client
from binance import ThreadedWebsocketManager

# api_key = os.environ.get('binance_api')
api_key = 'ygLyQROn7y7SdNvMoJepOdhZJV4OJUPeq1hhYe2929CopY2ZqGREhnWnVy1FQMEs'
# api_secret = os.environ.get('binance_secret')
api_secret = 'aACSH2BCvZKNwp7bbQR5vtMOJAGMvJ8SUB2Cdfw5sBF1g8sRjhRevQfu6EYpssKC'
client = Client(api_key=api_key, api_secret=api_secret, tld='com')

client.ping()

client.get_system_status()

account = client.get_account()

print(account)

current_price = float(client.get_symbol_ticker(symbol="BTCUSDT")["price"])

print('>>>', current_price)


def stream_data(msg):
    time = pd.to_datetime(msg["E"], unit="ms")
    price = msg["c"]
    print('Time: {} | Price: {}'.format(time, price))


# Starting the WebSocket
twm = ThreadedWebsocketManager()
twm.start()

# Subscribe to the stream
twm.start_symbol_miniticker_socket(callback=stream_data, symbol="BTCUSDT")

# twm.stop()
