class BankAcct:
    def __init__(self, name, account_number, amount, interest_rate):
        self.name = name
        self.account_number = account_number
        self.amount = amount
        self.interest_rate = interest_rate

    def adjust_interest_rate(self, new_rate):
        self.interest_rate = new_rate

    def withdraw(self, amount):
        if amount > self.amount:
            print("Insufficient balance")
        else:
            self.amount -= amount

    def deposit(self, amount):
        self.amount += amount

    def balance(self):
        return self.amount

    def calculate_interest(self, days):
        return (self.amount * self.interest_rate * days) / 365

    def __str__(self):
        return f"Name: {self.name}, Account Number: {self.account_number}, Balance: {self.amount}, Interest Rate: {self.interest_rate}"


def test_bank_account():
    print("Create account:")
    acct = BankAcct("S. Fisher", 234432525, 5000, 0.03)
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


main()
