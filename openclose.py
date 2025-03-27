class PaymentProcessor:
    def process_payment(self, payment_type, amount):
        if payment_type == "credit_card":
            print(f"Processing credit card payment of {amount}")
        elif payment_type == "paypal":
            print(f"Processing PayPal payment of {amount}")

        elif payment_type == "google_wallet":
            print(f"Processing Google Wallet payment of {amount}")
        elif payment_type == "apple_pay":
            print(f"Processing Apple Pay payment of {amount}")
        elif payment_type == "bitcoin":
            print(f"Processing Bitcoin payment of {amount}")
        else:
            raise ValueError("Unsupported payment type")