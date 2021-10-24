"""Practice with dictionaries."""

__author__ = "730396458"

# Define your functions below


def count(start: list[str]) -> dict[str, int]:
    """Create dictionary where value is the number of times the key appears in a list."""
    name_count: dict[str, int] = {}
    i: int = 0
    while i < len(start):
        name_count[start[i]] = 0
        i += 1
    runthru: int = 0
    while runthru < len(start):
        if start[runthru] in name_count:
            name_count[start[runthru]] += 1 
        runthru += 1
    return name_count


def invert(a: dict[str, str]) -> dict[str, str]:
    """Returns a dictionary inverting keys and values."""
    val_list: list[str] = []
    key_list: list[str] = [] 
    for key in a:
        key_list.append(key)
        val_list.append(a[key])
    proof: dict[str, int] = count(val_list)
    for key in proof:
        if proof[key] > 1:
            raise KeyError("A repeated key is invalid.")
    result: dict[str, str] = {}
    i: int = 0
    while i < len(val_list):
        result[val_list[i]] = key_list[i]
        i += 1
    return result

# It returns a str which is the color that appears most frequently.
# If there is a tie for most popular color, return the color that appeared in the dictionary first.


def favorite_color(colors: dict[str, str]) -> str:
    """Return the most common favorite color."""
    colchoice: list[str] = []
    for key in colors:
        colchoice.append(colors[key])
    colorcho: dict[str, int] = count(colchoice)
    val_list: list[int] = []
    key_list: list[str] = [] 
    for key in colorcho:
        key_list.append(key)
        val_list.append(colorcho[key])
    values: int = len(val_list) - 1
    max_value: int = val_list[values]
    while values > 0:
        if max_value < val_list[values - 1]:
            max_value = val_list[values - 1]
        values -= 1
    result: dict[int, str] = {}
    i: int = 0
    while i < len(val_list):
        result[val_list[i]] = key_list[i]
        i += 1
    return result[max_value] 
    
    