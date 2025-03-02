#!/bin/python3
# Ceres Search


from pathlib import Path


def has_good_neighbour(coords: tuple, crossword: list) -> bool:

    good_neighbour = {
        "X": ["M"],
        "M": ["X","A"],
        "A": ["M","S"],
        "S": ["A"],
    }

    x,y = coords

    # coords to check:
    #   ?   ?   ?
    #   ?   x   ?
    #   ?   ?   ?

    up, down, left, right = True, True, True, True
    if x == 0:
        # can't go up
        up = False
    if x == len(crossword):
        # can't go down
        down = False
    if y == 0:
        # can't go left
        left = False
    if y == len(crossword):
        # can't go right
        right = False

    # top left:
    #if x == 0 or y == 0:
    #    top_left = True
    #else:
    #    top_left = ( crossword[x-1][y-1] in good_neighbour[ crossword[x][y] ] ) # this is true if top left is a good neighbour
    #print(top_left)

    invalid_char = "0"

    top_left    = crossword[x-1][y-1] if (up and left)      else invalid_char
    top         = crossword[x-1][y]   if (up)               else invalid_char
    top_right   = crossword[x-1][y+1] if (up and right)     else invalid_char

    left        = crossword[x][y-1]   if (left)             else invalid_char
    right       = crossword[x][y+1]   if (right)            else invalid_char

    bot_left    = crossword[x+1][y-1] if (down and left)    else invalid_char
    bot         = crossword[x+1][y]   if (down)             else invalid_char
    bot_right   = crossword[x+1][y+1] if (down and right)   else invalid_char

    neighbours = [
        top_left,
        top,
        top_right,
        left,
        right,
        bot_left,
        bot,
        bot_right
        ]

    for neighbour in neighbours:
        if neighbour != invalid_char:
            if neighbour in good_neighbour[ crossword[x][y] ]:
                #print(f"{neighbour} is a good neighbour for {crossword[x][y]}")
                print(f"{x}, {y} ({crossword[x][y]}) has good neighbors")
                return True
            else:
                #print(f"{neighbour} is not a good neighbour for {crossword[x][y]}")
                pass
        else:
            # Some boundary condition was hit, char is in either edges of the crossword
            pass

    print(f"{x}, {y} ({crossword[x][y]}) has no good neighbors")
    return False


def step(start: tuple, dir: tuple) -> tuple:
    """
    takes a step from the start in dir
    """


def solution() -> None:
    """
    Solution for Day 4
    """
    input_path = Path(__file__).parent / "input"
    crossword = []
    with open(input_path, "r") as infile:
        for line in infile:
            crossword.append(list(line.strip()))

    x_max = len(crossword) -1
    y_max = x_max

# solution_1 = part_one(input_path)
# solution_2 = part_two(input_path)

# print(f"Solution 1: {solution_1}")
# print(f"Solution 2: {solution_2}")

    has_good_neighbour((1,1),crossword)

    print("iterating over crossword")
    for row in range(x_max):
        for column in range(y_max):
            has_good_neighbour((row,column),crossword)

solution()
