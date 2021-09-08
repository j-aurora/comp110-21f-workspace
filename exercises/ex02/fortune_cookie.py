"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730396458"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

print("Your fortune cookie says... ")
fortune: int = int(randint(1, 16))
if fortune > 8:
    if fortune > 12:
        print("Mindfulness is a good way to ground yourself when life is buys. ")
    else: 
        print("To love and be loved is to feel the Sun in the darkness. ")
else:
    if fortune <= 4:
        print("When feeling stressed, take comfort in pets. ")
    else: 
        print("Your life is amazing, don't let one bad thing hold you back.")
