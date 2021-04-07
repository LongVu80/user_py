class User:
    def __init__(self, name, email):
        self.username = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdraw(self, amount):
        self.account_balance -= amount

    def user_account_balance(self):
        print(f"User: {self.username}, Balance: ${self.account_balance}")

    def transfer_money(self, other, amount):
        self.account_balance -= amount
        other.account_balance += amount

Anthony = User("Anthony Smith", "AnthonyS@gmail.com")
Linda = User("Linda Grey", "LindaG@gmail.com")


Anthony.make_deposit(200)
Anthony.make_deposit(500)
Anthony.make_deposit(300)
Anthony.make_deposit(700)
Anthony.make_withdraw(600)
Anthony.user_account_balance()


Linda.make_deposit(400)
Linda.make_deposit(600)
Linda.make_deposit(800)
Linda.make_withdraw(700)
Linda.user_account_balance()

Anthony.transfer_money(Linda, 400)
Anthony.user_account_balance()
Linda.user_account_balance()