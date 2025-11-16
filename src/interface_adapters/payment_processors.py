from ..use_cases.payment_gateway import PaymentGateway
from .payment_factory import register


@register("credit_card")
class CreditCardProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")


@register("paypal")
class PayPalProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")


@register("bitcoin")
class BitcoinProcessor(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing bitcoin payment of ${amount}")