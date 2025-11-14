from typing import Protocol


class PaymentProcessor(Protocol):
    def process_payment(self, amount):
        ...


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing credit card payment of ${amount}")


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        print(f"Processing PayPal payment of ${amount}")


class PaymentFactory:
    @staticmethod
    def create_payment_processor(payment_method):
        if payment_method == "credit_card":
            return CreditCardProcessor()
        elif payment_method == "paypal":
            return PayPalProcessor()
        else:
            raise ValueError("Invalid payment method")


class Order:
    def __init__(self, items, payment_processor):
        self.items = items
        self.payment_processor = payment_processor
        self.total = sum(item.price * item.quantity for item in items)

    def process_payment(self):
        self.payment_processor.process_payment(self.total)
        print("Payment processed successfully")


class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


if __name__ == "__main__":
    items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1), Item("Item 3", 5, 3)]

    payment_method = "credit_card"

    payment_processor = PaymentFactory.create_payment_processor(payment_method)

    order = Order(items, payment_processor)

    order.process_payment()