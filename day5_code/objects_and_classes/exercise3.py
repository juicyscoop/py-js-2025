class BankAccount:
    def __init__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount > 0:
            self.cash += amount

    def withdraw_cash(self, amount):
        withdraw_amount = None
        if amount > 0:
            if amount > self.cash:
                withdraw_amount = self.cash
                self.cash = 0
            else:
                self.cash -= amount
                withdraw_amount = amount
        return withdraw_amount

    def withdraw_cash_jakub(self, amount):
        if amount > 0.0:
            withdrawn = min(amount, self.cash)
            self.cash -= withdrawn
            return withdrawn
        else:
            raise ValueError("Částka musí být kladná.")

    def print_info(self):
        print(f"Account number: {self.number}; Account balance: {self.cash}")

acc1 = BankAccount(123)
acc1.print_info()

acc1.deposit_cash(100)
acc1.print_info()

withdraw_am = acc1.withdraw_cash(500)
print(f"Withdrawn: {withdraw_am}")
acc1.print_info()