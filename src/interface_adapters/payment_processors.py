from ..use_cases.payment_gateway import PaymentGateway


class CreditCardProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")


class PayPalProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")
