class Payment:
    def __init__(self, order, amount):
        self.order = order
        self.amount = amount
        self.status = 'Unpaid'

    def process_payment(self):
        self.status = 'Paid'

    def __repr__(self):
        return f"Payment(order={self.order}, amount={self.amount}, status={self.status})"
