from typing import Dict, Type
from payment_processor import PaymentProcessor


class PaymentFactory:
    def __init__(self):
        self._processors: Dict[str, Type[PaymentProcessor]] = {}

    def register_processor(
        self, payment_method: str, processor_class: Type[PaymentProcessor]
    ):
        self._processors[payment_method] = processor_class

    def create_payment_processor(self, payment_method: str) -> PaymentProcessor:
        processor_class = self._processors.get(payment_method)
        if not processor_class:
            raise ValueError("Invalid payment method")
        return processor_class()
