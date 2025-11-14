from src.entities.item import Item
from src.entities.order import Order
from src.use_cases.process_order import ProcessOrder
from src.interface_adapters.payment_factory import PaymentFactory
from src.interface_adapters.payment_processors import (
    CreditCardProcessor,
    PayPalProcessor,
)


if __name__ == "__main__":
    items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1), Item("Item 3", 5, 3)]

    order = Order(items)

    payment_method = "credit_card"

    factory = PaymentFactory()
    factory.register_processor("credit_card", CreditCardProcessor)
    factory.register_processor("paypal", PayPalProcessor)

    payment_processor = factory.create_payment_processor(payment_method)

    process_order_use_case = ProcessOrder(payment_processor)
    process_order_use_case.execute(order)

    print(f"Order status: {order.status}")
