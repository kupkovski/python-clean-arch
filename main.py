from item import Item
from order import Order
from payment_factory import PaymentFactory
from credit_card_processor import CreditCardProcessor
from paypal_processor import PayPalProcessor


if __name__ == "__main__":
    items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1), Item("Item 3", 5, 3)]

    payment_method = "credit_card"

    factory = PaymentFactory()
    factory.register_processor("credit_card", CreditCardProcessor)
    factory.register_processor("paypal", PayPalProcessor)

    payment_processor = factory.create_payment_processor(payment_method)

    order = Order(items, payment_processor)

    order.process_payment()