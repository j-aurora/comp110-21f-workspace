"""Finding duplicate letters in a word."""

__author__ = "730396458"

word: str = input("Enter a word: ")
answer: str = ""
i: int = len(word) - 1
p: int = len(word) - 1

while i >= 0:
    if p != i:
        if word[i] == word[p]:
            answer = "True"
    
        else:
            answer = "False"
        print("Found duplicate: " + answer)
        p = p - 1
    i = i - 1