"""Practice using  numeric operators with multiple inputs"""

__author__ = "730396458"

x_value: str = input("Left-hand side: ")
y_value: str = input("Right-hand side: ")
exp: str = int(x_value) ** int(y_value)
print(x_value + " ** " + y_value + " is " + str(exp)) 
div: float = float(x_value) / float(y_value)
print(x_value + " / " + y_value + " is " + str(div))
intd: int = int(x_value) // int(y_value)
print(x_value + " // " + y_value + " is " + str(intd))
mod: int = int(x_value) % int(y_value)
print(x_value + " % " + y_value + " is " + str(mod))