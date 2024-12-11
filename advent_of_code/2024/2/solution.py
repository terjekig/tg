#!/bin/python3
# Red-Nosed Reports

from pathlib import Path
from math import copysign

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

            # Check level's "direction"
            if line_arr[0] == line_arr[1]: # skip the level, it is not safe
                continue
            level_direction = copysign(1, (line_arr[1] - line_arr[0]) )

            # Check conditions
            prev_level = line_arr[0]
            current_level = 0

            safe = False
            for current_level in line_arr[1:]:
                diff = current_level - prev_level
                safe_diff = 1 <= abs(diff) <= 3 # Range from excercise

                if ( safe_diff and ( level_direction == copysign(1, diff) ) ): # in range and direction still matches
                    safe = True
                    prev_level = current_level
                else:
                    safe = False
                    break

            if safe: n_of_safe += 1



    return n_of_safe

def part_two(path: Path) -> list:
    '''
    Same as before but a single outlier does not make a whole level unsafe
    '''

    n_of_safe = 0

    with open(path, "r") as infile:

        for line in infile:
            line_arr = []
            for level in line.strip().split():
                line_arr.append(int(level))

            # Check level's "direction", but no skipping as it would consume a life but those will be subtracted later
            unique_line = list(dict.fromkeys(line_arr)) # removing duplicates  # TODO converting from list to set messes with order, dict maybe?. [85, 87, 88 ,94, 94] becomes [88, 85, 94, 87] with a set
            level_direction = copysign(1, (unique_line[1] - unique_line[0]) )

            # Check conditions
            prev_level = line_arr[0]
            current_level = 0
            lives = 1
            safe = False
            for current_level in line_arr[1:]:
                diff = current_level - prev_level
                safe_diff = 1 <= abs(diff) <= 3 # Range from excercise

                if ( safe_diff and ( level_direction == copysign(1, diff) ) ): # in range and direction still matches
                    safe = True
                    prev_level = current_level
                elif lives > 0:
                    print(f"Removing {current_level} from {line_arr}")
                    safe = True
                    lives -= 1
                    #prev_level = current_level # commented out because "It's like the bad level never happened!"
                else:
                    print(f"Dropping {line_arr}")
                    safe = False
                    break

            if safe: n_of_safe += 1



    return n_of_safe



def solution() -> None:
    """
    TODO
    """
    solution_1 = part_one(Path(__file__).parent / "input")
    solution_2 = part_two(Path(__file__).parent / "input")

    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")


solution()
