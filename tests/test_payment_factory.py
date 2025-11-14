import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from payment_factory import PaymentFactory
from credit_card_processor import CreditCardProcessor
from paypal_processor import PayPalProcessor


class TestPaymentFactory(unittest.TestCase):
    def setUp(self):
        self.factory = PaymentFactory()
        self.factory.register_processor("credit_card", CreditCardProcessor)
        self.factory.register_processor("paypal", PayPalProcessor)

    def test_create_credit_card_processor(self):
        processor = self.factory.create_payment_processor("credit_card")
        self.assertIsInstance(processor, CreditCardProcessor)

    def test_create_paypal_processor(self):
        processor = self.factory.create_payment_processor("paypal")
        self.assertIsInstance(processor, PayPalProcessor)

    def test_create_invalid_processor(self):
        with self.assertRaises(ValueError):
            self.factory.create_payment_processor("invalid_method")


if __name__ == "__main__":
    unittest.main()
