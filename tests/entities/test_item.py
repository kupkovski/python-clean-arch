import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.entities.item import Item


class TestItem(unittest.TestCase):
    def test_item_creation(self):
        item = Item("Test Item", 10.5, 2)
        self.assertEqual(item.name, "Test Item")
        self.assertEqual(item.price, 10.5)
        self.assertEqual(item.quantity, 2)


if __name__ == "__main__":
    unittest.main()
