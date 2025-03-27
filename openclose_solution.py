from abc import ABC, abstractmethod

# Step 1: Create an abstract class for Payment
class Payment(ABC):
    @abstractmethod
    def process(self, amount):
        pass

# Step 2: Implement concrete payment methods
class CreditCardPayment(Payment):
    def process(self, amount):
        print(f"Processing credit card payment of {amount}")

class PayPalPayment(Payment):
    def process(self, amount):
        print(f"Processing PayPal payment of {amount}")

class GoogleWalletPayment(Payment):
    def process(self, amount):
        print(f"Processing Google Wallet payment of {amount}")

class ApplePayPayment(Payment):
    def process(self, amount):
        print(f"Processing Apple Pay payment of {amount}")

class BitcoinPayment(Payment):
    def process(self, amount):
        print(f"Processing Bitcoin payment of {amount}")


# Step 3: Use dependency injection in PaymentProcessor
class PaymentProcessor:
    def __init__(self, payment: Payment):
        self.payment = payment

    def process_payment(self, amount):
        self.payment.process(amount)

# Step 4: Usage
credit_card = CreditCardPayment()
paypal = PayPalPayment()
GoogleWallet = GoogleWalletPayment()
ApplePay = ApplePayPayment()

processor1 = PaymentProcessor(credit_card)
processor1.process_payment(100)

processor2 = PaymentProcessor(paypal)
processor2.process_payment(200)

processor3 = PaymentProcessor(GoogleWallet)
processor3.process_payment(300)

processor4 = PaymentProcessor(ApplePay)
processor4.process_payment(400)




