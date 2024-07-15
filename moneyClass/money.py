from decimal import Decimal


class Money(Decimal):
    # The __new__ method is a special method in Python that's called when an object is created
    def __new__(cls, v, units="USD"):
        # Call the parent class's __new__ method and return the result
        return super(Money, cls).__new__(cls, v)

    # The __init__ method is called after the object is created to initialize it
    def __init__(self, v, units="USD"):
        # Store the units of the money
        self.units = units

    # The __add__ method defines the behavior of the + operator
    def __add__(self, other):
        # If the other operand is a Money object, add the two amounts and return a new Money object
        if isinstance(other, Money):
            return Money(super(Money, self).__add__(other), self.units)
        # If the other operand is not a Money object, add the amount to this Money object's amount and return a new
        # Money object
        else:
            return Money(super(Money, self).__add__(other))

    # The __sub__ method defines the behavior of the - operator
    def __sub__(self, other):
        # If the other operand is a Money object, subtract the other amount from this amount and return a new Money
        # object
        if isinstance(other, Money):
            return Money(super(Money, self).__sub__(other), self.units)
        # If the other operand is not a Money object, subtract the other amount from this Money object's amount and
        # return a new Money object
        else:
            return Money(super(Money, self).__sub__(other))

    # The __mul__ method defines the behavior of the * operator
    def __mul__(self, other):
        # If the other operand is a Money object, multiply the two amounts and return a new Money object
        if isinstance(other, Money):
            return Money(super(Money, self).__mul__(other), self.units)
        # If the other operand is not a Money object, multiply this Money object's amount by the other amount and
        # return a new Money object
        else:
            return Money(super(Money, self).__mul__(other))


def test_money_class():
    m1 = Money("12.12", "USD")
    m2 = Money("3.34", "USD")
    print("m1: ", m1, m1.units)
    print("m2: ", m2, m2.units)

    m3 = m1 + m2
    print("m1 + m2: ", m3, m3.units)

    m4 = m1 - m2
    print("m1 - m2: ", m4, m4.units)

    m5 = m1 * m2
    print("m1 * m2: ", m5, m5.units)


def main():
    test_money_class()


main()
