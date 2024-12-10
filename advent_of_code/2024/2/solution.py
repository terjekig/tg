#!/bin/python3
# Red-Nosed Reports

from pathlib import Path
from math import copysign

def first_solution(path: Path) -> list:
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



def solution() -> None:
    """
    TODO
    """
    solution_1 = first_solution(Path(__file__).parent / "input")

    print(solution_1)


solution()
