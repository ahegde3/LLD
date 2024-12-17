class Bill:
    def __init__(self, reservation):
        self.reservation = reservation
        self.total_bill_amount = self.compute_bill_amount()
        self.is_bill_paid = False

    def compute_bill_amount(self):
        return 100.0