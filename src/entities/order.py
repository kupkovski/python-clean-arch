from typing import List
from .item import Item


class Order:
    def __init__(self, items: List[Item]):
        self.items = items
        self.total = sum(item.price * item.quantity for item in items)
        self.status = "open"
