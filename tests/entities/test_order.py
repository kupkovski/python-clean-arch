import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.entities.item import Item
from src.entities.order import Order


class TestOrder(unittest.TestCase):
    def test_order_creation(self):
        items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1)]
        order = Order(items)
        self.assertEqual(order.total, 40)
        self.assertEqual(order.status, "open")


if __name__ == "__main__":
    unittest.main()
