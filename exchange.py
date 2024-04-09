# exchange.py
import json

class Exchange:
    def __init__(self):
        self.orders = []

    def place_order(self, order):
        self.orders.append(order)

    def get_orders(self):
        return json.dumps(self.orders)

# Usage
exchange = Exchange()
exchange.place_order("Buy BTC")
exchange.place_order("Sell BTC")
print("Orders:", exchange.get_orders())
