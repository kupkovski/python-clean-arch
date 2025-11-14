from typing import Dict, Type
from ..use_cases.payment_gateway import PaymentGateway


class PaymentFactory:
    def __init__(self):
        self._processors: Dict[str, Type[PaymentGateway]] = {}

    def register_processor(
        self, payment_method: str, processor_class: Type[PaymentGateway]
    ):
        self._processors[payment_method] = processor_class

    def create_payment_processor(self, payment_method: str) -> PaymentGateway:
        processor_class = self._processors.get(payment_method)
        if not processor_class:
            raise ValueError("Invalid payment method")
        return processor_class()
