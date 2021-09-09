"""Practice the if-then-else statements."""

choice: int = int(input("Entera number: "))
# A < 25
# B >= 25 and < 50
# C >75
# D >= 50 and <= 75
if choice < 25:
    print("A")
else:
    if choice < 50:
        print("B")
    else: 
        if choice > 75:
            print("C")
        else:
            print("D")
