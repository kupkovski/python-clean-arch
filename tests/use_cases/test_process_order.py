import unittest
from unittest.mock import Mock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.entities.item import Item
from src.entities.order import Order
from src.use_cases.process_order import ProcessOrder


class TestProcessOrder(unittest.TestCase):
    def test_process_order(self):
        items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1)]
        order = Order(items)

        mock_payment_gateway = Mock()
        process_order_use_case = ProcessOrder(mock_payment_gateway)
        process_order_use_case.execute(order)

        mock_payment_gateway.process_payment.assert_called_once_with(40)
        self.assertEqual(order.status, "paid")


if __name__ == "__main__":
    unittest.main()
