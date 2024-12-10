#!/bin/python3
# Red-Nosed Reports

from pathlib import Path
from math import copysign

def process_input(path: Path) -> list:
    '''
    I've pasted my puzzle's input to this input file
    '''

    n_of_safe = 0

    with open(path, "r") as infile:

        for line in infile:
            line_arr = []
            for level in line.strip().split():
                line_arr.append(int(level))

            # Check level's "direction"
            if line_arr[0] == line_arr[1]: # skip the level, it is not safe
                print(f"Skipping level since first 2 are equal")
                continue
            level_direction = copysign(1, (line_arr[1] - line_arr[0]) )

            # Check conditions
            prev_level = line_arr[0]
            current_level = 0

            safe = False
            for current_level in line_arr[1:]:
                diff = current_level - prev_level
                safe_diff = 1 <= abs(diff) <= 3

                if not safe_diff:
                    print(f"{line_arr} not safe because diff is {diff}")
                    safe = False
                    break

                if ( level_direction != copysign(1, diff) ):
                    print(f"{line_arr} not safe because direction is {level_direction} but current dir is {copysign(1, diff)}")
                    safe = False
                    break

                safe = True
                prev_level = current_level


            if safe: n_of_safe += 1



    return n_of_safe



def solution() -> None:
    """
    TODO
    """
    input_data = process_input(Path(__file__).parent / "input")

    print(input_data)


solution()
