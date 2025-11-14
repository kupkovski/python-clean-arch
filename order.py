from typing import List
from item import Item
from payment_processor import PaymentProcessor


class Order:
    def __init__(self, items: List[Item], payment_processor: PaymentProcessor):
        self.items = items
        self.payment_processor = payment_processor
        self.total = sum(item.price * item.quantity for item in items)

    def process_payment(self):
        self.payment_processor.process_payment(self.total)
        print("Payment processed successfully")
