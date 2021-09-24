"""Example of writing a function to procss a list."""


def main() -> None:
    """Entrypoint."""
    names: list[str] = ["Kris", "Kaki"]
    print(contains("Kevin", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Returns True iff needle is found in a haystack, False otherwise."""
    i: int = 0
    while i < len(haystack):
        item: str = haystack[i] 
        # As soon as needle is found return True
        if item == needle:
            return True
        i += 1

    return False
   
    
if __name__ == "__main__":
    main() 