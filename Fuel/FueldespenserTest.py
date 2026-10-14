import unittest

from Fuel.Fuel_despenser import FuelDespenser


class FuelingStationTest(unittest.TestCase):

    def setUp(self):
        self.fuel = FuelDespenser()

    def test_petrol_price_is_650(self):
        self.assertEqual(650, self.fuel.get_price("Petrol"))

    def test_diesel_price_is_720(self):
        self.assertEqual(720, self.fuel.get_price("Diesel"))

    def test_kerosene_price_is_550(self):
        self.assertEqual(550, self.fuel.get_price("Kerosene"))

    def test_gas_price_is_480(self):
        self.assertEqual(480, self.fuel.get_price("Gas"))

    def test_kerosene_2_liters_cost_1100(self):
        result = self.fuel.calculate_cost("Kerosene", 2)

        self.assertEqual(1100, result)

    def test_gas_5_liters_cost_2400(self):
        result = self.fuel.calculate_cost("Gas", 5)

        self.assertEqual(2400, result)

    def test_that_I_can_buy_4_liters_of_kerosene(self):
        result = self.fuel.calculate_liters("Kerosene", 2200)

        self.assertEqual(4, result)

    def test_2400_can_buy_5_liters_of_gas(self):
        result = self.fuel.calculate_liters("Gas", 2400)

        self.assertEqual(5, result)

    def test_buying_2_liters_of_kerosene_records_transaction(self):
        transaction = self.fuel.buy_by_liters("Kerosene", 2)

        self.assertEqual("Kerosene", transaction["product"])
        self.assertEqual(1100, transaction["amount"])
        self.assertEqual(2, transaction["liters"])

    def test_cannot_buy_zero_liters(self):
        with self.assertRaises(ValueError):
            self.fuel.calculate_cost("Petrol", 0)

    def test_cannot_buy_negative_liters(self):
        with self.assertRaises(ValueError):
            self.fuel.calculate_cost("Petrol", -10)

    def test_cannot_buy_more_than_50_liters(self):
        with self.assertRaises(ValueError):
            self.fuel.calculate_cost("Petrol", 51)

    def test_can_buy_exactly_1_liter(self):
        result = self.fuel.calculate_cost("Petrol", 1)

        self.assertEqual(650, result)


if __name__ == '__main__':
    unittest.main()