import unittest
from unittest.mock import Mock
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from order import Order
from item import Item


class TestOrder(unittest.TestCase):
    def setUp(self):
        self.items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1)]

    def test_order_total_calculation(self):
        mock_processor = Mock()
        order = Order(self.items, mock_processor)
        self.assertEqual(order.total, 40)

    def test_process_payment(self):
        mock_processor = Mock()
        order = Order(self.items, mock_processor)
        order.process_payment()
        mock_processor.process_payment.assert_called_once_with(40)


if __name__ == "__main__":
    unittest.main()
