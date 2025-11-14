from typing import Protocol


class PaymentProcessor(Protocol):
    def process_payment(self, amount: float) -> None:
        ...
