class payment:
    def pay(self,amount):
        pass
class cashpayment(payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} in cash")
class cardpayment(payment):
    def pay(self,amount):
        print(f"Paid ₹{amount} using credit/debit card")
class upipayment(payment):
    def pay(self,amount):
        print(f"paid ₹{amount} using UPI")

payments = [cashpayment(), cardpayment(), upipayment()]

for payment in payments:
    payment.pay(1000)
