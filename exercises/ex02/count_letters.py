"""Counting letters in a string."""

__author__ = "730396458"


letter: str = input("What letter do you want to search for?: ")
word: str = input("Enter a word: ")
count: int = 0
i: int = len(word) - 1 

while i >= 0:
    if word[i] == letter:
        count = count + 1
        i = i - 1
    else:
        i = i - 1

print("Count: " + str(count)) 
