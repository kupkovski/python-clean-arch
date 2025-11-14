from src.entities.item import Item
from src.entities.order import Order
from src.use_cases.process_order import ProcessOrder
from src.interface_adapters.payment_factory import factory

# By importing the payment_processors module, the classes within it will be
# discovered and the @register decorator will automatically register them with the factory.
from src.interface_adapters import payment_processors


if __name__ == "__main__":
    items = [Item("Item 1", 10, 2), Item("Item 2", 20, 1), Item("Item 3", 5, 3)]

    order = Order(items)

    payment_method = "credit_card"

    # The factory is now populated automatically by the decorators.
    # No manual registration is needed.
    payment_processor = factory.create_payment_processor(payment_method)

    process_order_use_case = ProcessOrder(payment_processor)
    process_order_use_case.execute(order)

    print(f"Order status: {order.status}")