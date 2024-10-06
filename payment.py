class Payment:
    def __init__(self, amount):
        self.amount = amount
        self.status = "Pending"

    def process_payment(self):
        self.status = "Completed"
        print(f"Payment of ${self.amount} has been processed.")

    def send_reminder(self):
        print(f"Reminder: Payment of ${self.amount} is due.")

    def apply_penalty(self, penalty_amount):
        self.amount += penalty_amount
        print(f"A penalty of ${penalty_amount} has been applied. New amount: ${self.amount}.")
