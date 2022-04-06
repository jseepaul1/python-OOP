# chaining methods
# Update your previous assignment so that each instance's methods are chained
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
        return self

    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount) 
        other_user.make_deposit(amount) 
        return self

guido = User("Guido", "guido@python.com")
monty = User("Monty", "monty@python.com") 
argo = User("Argo", "argo@gmail.com") 

guido.make_deposit(1000).make_deposit(200).make_deposit(500).make_withdrawal(300).display_user_balance()
monty.make_deposit(500).make_deposit(700).make_withdrawal(100).make_withdrawal(150).display_user_balance()
argo.make_deposit(2000).make_withdrawal(50).make_withdrawal(150).make_withdrawal(200).display_user_balance()

guido.transfer_money(300, argo).display_user_balance()
guido.display_user_balance()