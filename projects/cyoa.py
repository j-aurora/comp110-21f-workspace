"""Create an adventure, what type of houseplant are you."""

points: int = 0
player: str = ""


def main() -> None:
    greet()


def greet() -> None: 
    """Greet the player.""" 
    print("Welcome to this little quiz. ")
    player = input("What would you like to be called? ")
    print("Do want to continue?" + player)
    choice_1: str = input("(Enter No, Yes, or Tell me more) ")
    if choice_1 == "No":
        print("I'm sorry to see you go." )
        print(points)


def Que1(x: str) -> str:



if __name__ == "__main__":
    main()