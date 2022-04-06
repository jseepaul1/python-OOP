# make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
# display_user_balance(self) - have this method print the user's name and account balance to the terminal
# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawal(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, amount, other_user):
        self.make_withdrawal(amount) #first user account
        other_user.make_deposit(amount) #third user account


guido = User("Guido", "guido@python.com") #first instance
guido.make_deposit(1000)
guido.make_deposit(200)
guido.make_deposit(500)
guido.make_withdrawal(300)
guido.display_user_balance()

monty = User("Monty", "monty@python.com") #second instance
monty.make_deposit(500)
monty.make_deposit(700)
monty.make_withdrawal(100)
monty.make_withdrawal(150)
monty.display_user_balance()

argo = User("Argo", "argo@gmail.com") #third instance
argo.make_deposit(2000)
argo.make_withdrawal(50)
argo.make_withdrawal(150)
argo.make_withdrawal(200)
argo.display_user_balance()

guido.transfer_money(300, argo) #transfer from first user to third user
guido.display_user_balance()
argo.display_user_balance()
