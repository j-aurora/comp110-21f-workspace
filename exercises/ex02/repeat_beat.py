"""Repeating a beat in a loop."""

__author__ = "730396458"

beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
i: int = 1

if repeat < 1:
    print("No beat... ")
else:
    while i < repeat:
        i = i + 1
        beat = beat + (" ") + beat 
    print(beat)
