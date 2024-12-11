#!/bin/python3
# Red-Nosed Reports

from pathlib import Path
from math import copysign

def check_level(level_array: list) -> bool:
    """
    Checking the level should be a separate function because I'll iterate on the same level multiple times
    """

    # Check level's "direction"
    if level_array[0] == level_array[1]: # skip the level, it is not safe
        return False
    level_direction = copysign(1, (level_array[1] - level_array[0]) )

    # Check conditions
    prev_level = level_array[0]
    current_level = 0

    for current_level in level_array[1:]:
        diff = current_level - prev_level
        safe_diff = 1 <= abs(diff) <= 3 # Range from excercise

        if ( safe_diff and ( level_direction == copysign(1, diff) ) ): # in range, direction still matches
            prev_level = current_level
        else:
            return False

    return True

def part_one(path: Path) -> list:
    '''
    File's contents are levels, they have a boundary of change that is safe, and the change's direction must remain constant in a line
    '''

    n_of_safe = 0

    with open(path, "r") as infile:

        for line in infile:
            line_arr = []
            for level in line.strip().split():
                line_arr.append(int(level))

            if check_level(line_arr): n_of_safe += 1

    return n_of_safe

def part_two(path: Path) -> list:
    '''
    Same as before but a single outlier does not make a whole level unsafe.
    Checking every line without every level once. If any of them is safe, the level is safe.
    '''

    n_of_safe = 0

    with open(path, "r") as infile:

        for line in infile:
            line_arr = []
            for level in line.strip().split():
                line_arr.append(int(level))

            new_list = []
            safe = False
            for i, _ in enumerate(line_arr): 
                new_list = line_arr[:i] + line_arr[i+1:] # Making a new list without line[i]
                safe = check_level(new_list)
                if safe: break

            if safe: n_of_safe += 1

    return n_of_safe



def solution() -> None:
    """
    Solution for Day 2
    """
    solution_1 = part_one(Path(__file__).parent / "input")
    solution_2 = part_two(Path(__file__).parent / "input")

    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")


solution()
