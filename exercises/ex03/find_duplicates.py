"""Finding duplicate letters in a word."""

__author__ = "730396458"

word: str = input("Enter a word: ")
answer: str = ""
i: int = len(word) - 1
p: int = len(word) - 1

while i >= 0:
    while p >= 0:
        if word[i] == word[p]:
            answer = "True"
        else: 
            answer = "False"
        p = p - 1
    i = i - 1

print("Found duplicate: " + answer)
