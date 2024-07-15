from decimal import Decimal

class Money(Decimal):
    def __new__(cls, v, units="USD"):
        return super(Money, cls).__new__(cls, v)

    def __init__(self, v, units="USD"):
        self.units = units

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(super(Money, self).__add__(other), self.units)
        else:
            return Money(super(Money, self).__add__(other))

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(super(Money, self).__sub__(other), self.units)
        else:
            return Money(super(Money, self).__sub__(other))

class BankAcct(Money):
    def __new__(cls, v, name, account_number, interest_rate):
        return super(BankAcct, cls).__new__(cls, v)

    def __init__(self, v, name, account_number, interest_rate):
        super().__init__(v)
        self.name = name
        self.account_number = account_number
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        if Money(amount) > self:
            print("Insufficient balance")
        else:
            self -= Money(amount)

    def deposit(self, amount):
        self += Money(amount)

    def balance(self):
        return self

    def calculate_interest(self, days):
        return (self * Decimal(self.interest_rate) * Decimal(days)) / Decimal(365)

    def __str__(self):
        return f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self}, Interest Rate: {self.interest_rate}"

def test_bank_account():
    print("Create account:")
    acct = BankAcct(5000, "S. Fisher", 234432525, 0.03)
    print(acct)
    print("Deposit 5000 into account:")
    acct.deposit(5000)
    print(acct)
    print("Withdraw 2000 from account:")
    acct.withdraw(2000)
    print(acct)
    print("Adjust interest rate:")
    acct.adjust_interest_rate(0.05)
    print(acct)
    print("Calculate interest rate over time:")
    interest = acct.calculate_interest(30)
    print(f"Interest for 30 days: {interest}")

def main():
    test_bank_account()

if __name__ == "__main__":
    main()
