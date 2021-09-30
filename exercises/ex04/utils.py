"""List utility functions."""

__author__ = "730396458"


def all(nums: list[int], match: int) -> bool:
    """Should return True if all values in a list match the int given."""
    i: int = len(nums) - 1
    while i >= 0:
        if match == nums[i]:
            i -= 1
        else:
            return False
    return True


def is_equal(ent1: list[int], ent2: list[int]):
    """Return True if every element is equal at all places."""
    m: int = len(ent1) - 1
    n: int = len(ent2) - 1
    i: int = 0
    if m != n: 
        return False
    if m == n: 
        while i <= n:
            if ent1[i] == ent2[i]:
                i += 1
            else:
                return False
        return True
   
        
def max(input: list[int]) -> int:
    """Find and return max value in a function."""
    if len(input) == 0: 
        raise ValueError("max() arg is an empty List") 
    values: int = len(input) - 1
    max_value: int = input[values]
    while values > 0:
        if max_value < input[values - 1]:
            max_value = input[values - 1]
        values -= 1
    return max_value