# Assignment: Users with Bank Accounts
from bank_account import BankAccount
class User:
    def __init__(self, name, email, amount):
        self.name = name
        self.email = email
        self.balance += amount

    def make_deposit(self, amount):
        self.balance += amount

    def make_withdrawal(self, amount):
        self.balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")

    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount) 
        other_user.make_deposit(amount) 


guido = User("Guido", "guido@python.com")
monty = User("Monty", "monty@python.com") 
argo = User("Argo", "argo@gmail.com") 



