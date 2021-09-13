"""An exercise in remainders and boolean logic."""

__author__ = "730396458"

divis: str = ""
given: int = int(input("Enter an int: "))
if (given % 2) == 0 or (given % 7) == 0:
    if (given % 2) == 0:
        divis = divis + "TAR "
        if (given % 7) == 0:
            divis = divis + "HEELS"
        print(divis)
    else:
        if (given % 7) == 0:
            divis = divis + "HEELS"
            print(divis)
else:
    print("CAROLINA")