class Bank:
    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000
    
    def get_blance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        
    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'You Can Withdraw below {self.min_withdraw}')
            return f'You Can Withdraw below {self.min_withdraw}'
        elif amount > self.max_withdraw:
            print(f'You can not with more then {self.max_withdraw}')
            return f'You can not with more then {self.max_withdraw}'
        else:
            self.balance -= amount
            print(f'Here is Your Money {amount}')
            print(f'Your balance after withdraw {self.get_blance()}')

brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(15000000)
brac.withdraw(1000)