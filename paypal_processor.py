from payment_processor import PaymentProcessor


class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing PayPal payment of ${amount}")
