# Assignment: Users with Bank Accounts
from bank_account import BankAccount


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.bank_accounts = dict()

    def make_deposit(self, bank_account_id, amount):
        bank_account = self.bank_accounts[bank_account_id]
        bank_account.deposit(amount)
        print(f'You new balance for account id {bank_account_id} is ${bank_account.balance}')
        return self

    def make_withdrawal(self, bank_account_id, amount):
        bank_account = self.bank_accounts[bank_account_id]
        bank_account.withdraw(amount)
        print(f'You new balance after withdrawal for account id {bank_account_id} is ${bank_account.balance}')
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self

    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self

    def create_account(self, int_rate, balance):
        bank_account = BankAccount(int_rate, balance)
        self.bank_accounts.update({bank_account.id: bank_account})
        print(f'Your new account was created successfully! New account id is {bank_account.id}')
        return bank_account.id
        


guido = User("Guido", "guido@python.com")
account_id_1 = guido.create_account(0.03, 200)
account_id_2 = guido.create_account(0.04, 500)
account_id_3 = guido.create_account(0.05, 1000)

guido.make_deposit(account_id_2, 300)

guido.make_deposit(account_id_1, 100).make_deposit(account_id_1, 200).make_deposit(account_id_1, 300).make_withdrawal(account_id_1,150)

guido.make_deposit(account_id_3, 600).make_deposit(account_id_3, 100).make_withdrawal(account_id_3,100)
