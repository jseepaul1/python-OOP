# Assignment: BankAccount
class BankAccount:
    bank_accounts = []

    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance
        self.bank_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= 0:
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee ")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance * self.int_rate
        else:
            print('You have a negative balance')
        return self

    @classmethod
    def bank_account_info(cls):
        for account in cls.bank_accounts:
            account.display_account_info()


account1 = BankAccount(0.03, 200)
account2 = BankAccount(0.06, 250)

account1.deposit(200.12).deposit(200).deposit(100).withdraw(500).yield_interest()
account2.deposit(1000).deposit(400).withdraw(50).withdraw(100).withdraw(140).withdraw(21.15).yield_interest()

account1.display_account_info()
account2.display_account_info()
BankAccount.bank_account_info()
