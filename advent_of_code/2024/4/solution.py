#!/bin/python3
# Ceres Search


from pathlib import Path


def has_good_neighbor(coords: tuple, crossword: list) -> bool:

    good_neighbor = {
        "X": ["M"],
        "M": ["X","A"],
        "A": ["M","S"],
        "S": ["A"],
    }

    x,y = coords
    print(crossword[x][y])


    return False


def solution() -> None:
    """
    Solution for Day 4
    """
    input_path = Path(__file__).parent / "input"
    crossword = []
    with open(input_path, "r") as infile:
        for line in infile:
            crossword.append(list(line.strip()))

# solution_1 = part_one(input_path)
# solution_2 = part_two(input_path)

# print(f"Solution 1: {solution_1}")
# print(f"Solution 2: {solution_2}")

    has_good_neighbor((0,1),crossword)

solution()
