"""Repeating a beat in a loop."""

__author__ = "730396458"

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i: int = 1
full_beat: str = ""

while i <= repeat:
    if 1 < 1:
        print("No beat... ")
    else:
        i = i + 1
        full_beat = full_beat + beat + (" ")
    
print(full_beat)
