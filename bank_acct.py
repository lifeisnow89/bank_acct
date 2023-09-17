class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=.03, balance=0)
    
    def make_deposit(self, amount):
        self.account.make_deposit(amount)
        return self

    def withdrawal(self, amount):
        self.account.withdrawal(amount)
        return self

    def display_user_balance(self):
        print(self.name)
        print(self.email)
        self.account.display_account_info()
        return self

class BankAccount:
    accounts = []
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)


    def make_deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if(self.balance - amount)>= 0:
            self.balance -=amount
        else:
            print(f"Insufficient Funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance{self.balance}")

    def display_user_balance(self):
        print(self.name)
        print(self.balance)
        self.account.display_account_info()
        return self


user_one = User("Gregory", "g@hmail.com")
user_one.make_deposit(500).display_user_balance().withdrawal(250).display_user_balance()

