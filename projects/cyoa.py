"""Create an adventure."""

__author__ = '730396458'

import random
points: int = 0
player: str = ""
STAR_EYES: str = '\U0001F929'
SAD_FACE: str = '\U0001F614'
SMALL_PLANT: str = '\U0001F331'
pots: list[str] = ["blue", "purple", "orange", "green", "terracotta", "turquiose"]


def main() -> None:
    points: int = 0
    i: int = 1
    while i > 0:
        greet()
        print(points)
        again: str = input("Play again? ")
        if again == "no" or again == "No":
            print(f"A {random.choice(pots)} pot would have looked nice. ")
            i = 0


def greet() -> None: 
    """Greet the player.""" 
    print("Welcome to this little quiz. ")
    player = input("What is your name? ")
    print(f"Do want to continue, {player}? ")
    print(STAR_EYES)
    choice_1: str = input("(Enter No, Yes, or Tell me more) ")
    if choice_1 == "No":
        print(f"I'm sorry to see you go. {SAD_FACE}")
        print(f"You have {points} points.")
    if choice_1 == "Tell me more":
        tell_more()
    if choice_1 != "No":
        Q_1()


def tell_more():
    """Explain the purpose of this program."""
    print("This is a little quiz to help you decide what houseplant is right for you! ")
    print(SMALL_PLANT)
    Q_1()


def Q_1():
    """Question 1."""
    print("Do you have pets where you live? ")
    points: int = 0
    if input("cat, dog, or neither? ") == "neither":
        points = points - 1 
    else: 
        points = points + 3
    pts: int = water(light(points))
    result(pts)
    

def light(p: int) -> int:
    """Can you provide the right lighting?"""
    light: int = int(input("How many hours of light comes through your windows during the day? "))
    if light > p:
        p = p - 3
    else:
        p = p + 3
    return p 


def water(p: int) -> int:
    """Will you water it right?"""
    wet: str = input("Will you forget to water your plant? yes or no ")
    if wet == "yes":
        p = p - 2
    else:
        p = p + 3 
    return p
    

def result(pts: int):
    if pts > 7: 
        if pts > 10:
            print("You should get an orchid. ")
        else:
            print("Yous hsould get a money plant. ")
    else:
        if pts > 4:
            print("You should get a succulent. ")
        else:
            print("You should get a pothos. ")


if __name__ == "__main__":
    main()