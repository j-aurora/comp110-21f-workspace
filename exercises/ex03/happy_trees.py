"""Drawing forests in a loop."""

__author__ = "730396458"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'
stack: int = int(input("Depth: "))
i: int = 0
tree_line: str = ""

while i < stack:
    tree_line = tree_line + TREE
    print(tree_line)
    i = i + 1
