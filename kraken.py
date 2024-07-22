import ccxt
import time


# import ccxt.kraken

exchange_params = {
    "API_KEY": "apik",
    "API_KEY_SECRET": "xyz",
    "TESTNET": True,
}

exchange = ccxt.krakenfutures(
    {
        "apiKey": exchange_params["API_KEY"],
        "secret": exchange_params["API_KEY_SECRET"],
        "enableRateLimit": True,
        'options': {
            'defaultType': 'future',
        },
    }
)

# if you are using testnet
exchange.set_sandbox_mode(True)
balance = exchange.fetch_balance({"type": "future","marginType": "isolated"})

# u can get the symbols from here
market = exchange.load_markets()
print(market)

symbol = "BTC/USD:BTC"

# current price of asset BTC : $59000
current_price = exchange.fetch_ticker(symbol)

# note: the price is in usd u can calculate the price in btc by dividing the price by the current price of btc

# market order of 1usd
market_order = exchange.create_order(symbol, 'market', 'buy', 1)


# place limit buy order for 0. 001 BTC at $60000
limit_order = exchange.create_order(symbol, 'limit', 'buy', 1,60000)


# place conditional order 1
# place stop - loss order for 0. 001 BTC at $58000
sl_order = exchange.create_order(symbol, 'limit', 'sell', 1,None,{"stopLossPrice": "58000","reduceOnly": True})


# place conditional order 2
# place take - profit order for 0. 001 BTC at $61000
tp_order = exchange.create_order(symbol, 'limit', 'sell', 1,None,{"takeProfitPrice": "70000","reduceOnly": True})

