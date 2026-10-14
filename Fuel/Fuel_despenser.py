from datetime import datetime


class FuelDespenser:

    def __init__(self):
        self.fuels = {"Petrol": 650,"Diesel": 720,"Kerosene": 550,"Gas": 480}

        self.transactions = []
    def display_fuels(self):
        for number, fuel in enumerate(self.fuels, start = 1):
            price = self.fuels[fuel]
            print(f"{number}. {fuel} => ₦{price} / Liter")

    def get_price(self, fuel):
        if fuel not in self.fuels:
            raise ValueError("Invalid fuel type")

        return self.fuels[fuel]

    def calculate_cost(self, fuel, liters):
        price = self.get_price(fuel)

        if liters < 1 or liters > 50:
            raise ValueError("Liters must be between 1 and 50")

        return price * liters

    def calculate_liters(self, fuel, amount):
        price = self.get_price(fuel)

        if amount <= price:
            raise ValueError("Amount must be above the price of one liter")

        liters = amount / price

        if liters > 50:
            raise ValueError("Amount cannot buy more than 50 liters")

        return liters

    def buy_by_liters(self, fuel, liters):
        amount = self.calculate_cost(fuel, liters)

        transaction = {"product": fuel,"amount": amount,"liters": liters,"date": datetime.now().strftime("%d/%m/%Y")}

        self.transactions.append(transaction)

        return transaction

    def buy_by_amount(self, fuel, amount):
        liters = self.calculate_liters(fuel, amount)

        transaction = {"product": fuel,"amount": amount,"liters": liters,"date": datetime.now().strftime("%d/%m/%Y")}

        self.transactions.append(transaction)

        return transaction

    def generate_receipt(self, transaction):
        receipt = f"""
Customers Transaction Receipt
=   Product : {transaction['product']}
=   Amount  : ₦{transaction['amount']}
=   Liters  : {transaction['liters']:.2f}L
=   Thank you for your Patronage
"""
        return receipt

    def show_transaction_history(self):
        if len(self.transactions) == 0:
            return "No transactions yet."

        history = "All Transactions\n"

        for transaction in self.transactions:
            history += f"""
=   Product : {transaction['product']}
=   Amount  : ₦{transaction['amount']}
=   Liters  : {transaction['liters']:.2f}L
=   Date    : {transaction['date']}
"""

        return history