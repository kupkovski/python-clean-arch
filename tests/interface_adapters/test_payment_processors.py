import unittest
import sys
import os
import io
from contextlib import redirect_stdout

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.interface_adapters.payment_processors import (
    CreditCardProcessor,
    PayPalProcessor,
)


class TestPaymentProcessors(unittest.TestCase):
    def test_credit_card_processor(self):
        processor = CreditCardProcessor()
        with io.StringIO() as buf, redirect_stdout(buf):
            processor.process_payment(100)
            output = buf.getvalue().strip()
        self.assertEqual(output, "Processing credit card payment of $100")

    def test_paypal_processor(self):
        processor = PayPalProcessor()
        with io.StringIO() as buf, redirect_stdout(buf):
            processor.process_payment(200)
            output = buf.getvalue().strip()
        self.assertEqual(output, "Processing PayPal payment of $200")


if __name__ == "__main__":
    unittest.main()
