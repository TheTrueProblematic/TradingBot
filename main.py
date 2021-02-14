from bot import pumpBot
import shrimpy
import time

exchange_public_key = 'o9pweDdKtniUw2uF94Sl87V4pThUWggSvPHmSw2xI4OrIsElhHTJSYAI9A3NeCYa'
exchange_secret_key = 'TJWj7QHdUNkgCHZbPky7lo0dAMEiMrMGz3LVrQJWcYjCWwFayelCwxFQMRvXz6sp'
shrimpy_public_key = 'eb3b30e4cceb52907166182a1b7c718fa39e3c7e206c9ab7dc0d6486f234a176'
shrimpy_secret_key = '1d926f3bcbff631b0e8b93aad9cc7d3c0d886ad5b9e3589e86669a59d31f2fad784f8cbadcd009bd951ee630971ff0fbc6bc20c0dfd7da020e9a65ce097c6418'
user_id = 'cbc3dd48-e823-472c-a7e6-2219ed8fe0bb'
account_id = '67114'

pumpy = pumpBot(exchange_public_key, exchange_secret_key, shrimpy_public_key, shrimpy_secret_key, user_id, account_id)

# pumpy.print("test", "test")


def error_handler(err):
    pumpy.error_handler(err)


raw_token = pumpy.getRawToken()
ws_client = shrimpy.ShrimpyWsClient(error_handler, raw_token['token'])
boughtAt = 0
margin = 2


def handler(msg):
    global boughtAt
    global coin
    global pumpy
    pric = msg['content'][0]['price']
    price = float(pric)
    pumpy.print("Price", str(price))
    if boughtAt == 0:
        pumpy.condense(coin)
        boughtAt = price
        pumpy.print("Bought At", str(price))
    elif price > (boughtAt * margin) or price < (boughtAt * 0.9):
        pumpy.condense('BTC')
        pumpy.endPrintStream()
        pumpy.print("Sold For", str(price))
        ws_client.disconnect()


coin = pumpy.coinPrompt()
coinPair = coin + "-btc"
subscribe_data = {
    "type": "subscribe",
    "exchange": "binance",
    "pair": coinPair,
    "channel": "trade"
}
pumpy.startPrintStream()
ws_client.connect()
ws_client.subscribe(subscribe_data, handler)
