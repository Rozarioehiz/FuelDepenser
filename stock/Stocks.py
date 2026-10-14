class Stock:
    def __init__(self, stock, current_price):
        self._stock = stock
        self._current_price = current_price

    def get_stock(self, current_price):
        return self._current_price