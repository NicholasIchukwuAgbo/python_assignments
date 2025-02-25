import unittest
from expense_tracker import (get_date,get_description,get_amount,calculate_total_expenses)

class TestExpenseTrackerApp(unittest.TestCase):

    def test_get_date_valid(self):
        self.assertTrue(get_date("01/01/2022"))

    def test_get_date_invalid_format(self):
        self.assertFalse(get_date("04-05-2003"))

    def test_get_description_valid(self):
        self.assertTrue(get_description("Test description"))

    def test_get_description_empty(self):
        self.assertFalse(get_description(""))

    def test_get_amount_valid(self):
        self.assertTrue(get_amount(10.99))

    def test_amount_is_less_than_one(self):
        self.assertFalse(get_amount(0.99))

    def test_calculate_total_expenses(self):
        amount_holder = [10.99, 20.99, 30.99]
        self.assertEqual(calculate_total_expenses(amount_holder), 62.97)


if __name__ == "__main__":
    unittest.main()
