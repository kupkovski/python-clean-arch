from payment_processor import PaymentProcessor


class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> None:
        print(f"Processing credit card payment of ${amount}")
