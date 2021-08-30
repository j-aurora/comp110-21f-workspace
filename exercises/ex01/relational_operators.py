"""Part 3 of EX01: practice using relational operators."""

__author__ = "730396458"

x_value: str = input("Left-hand side: ")
y_value: str = input("Right-hand side: ")
less_than: int = int(x_value) < int(y_value)
at_least: int = int(x_value) >= int(y_value)
eq: int = int(x_value) == int(y_value)
no_eq: int = int(x_value) != int(y_value)
print(x_value + " < " + y_value + " is " + str(less_than))
print(x_value + " >= " + y_value + " is " + str(at_least))
print(x_value + " == " + y_value + " is " + str(eq))
print(x_value + " != " + y_value + " is " + str(no_eq))