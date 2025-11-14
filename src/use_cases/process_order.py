from ..entities.order import Order
from .payment_gateway import PaymentGateway


class ProcessOrder:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def execute(self, order: Order):
        self.payment_gateway.process_payment(order.total)
        order.status = "paid"
        print("Payment processed successfully")
