#!/bin/python3
# Red-Nosed Reports

from pathlib import Path


def process_input(path: Path) -> list:
    '''
    I've pasted my puzzle's input to this input file
    '''

    input_list = []


    with open(path, "r") as infile:
        n_of_safe = 0
        increasing = False

        for line in infile:
            line_arr = []
            safe = False
            line_arr.append([int(x) for x in line.split()])

            if line_arr[0] <= line_arr[1]: # check for equal
                increasing = False
            else:
                increasing = True

            prev_level = line_arr[0]
            current_level = 0
            for current_level in line_arr[1:]:
                diff = current_level - prev_level
                safe = False if ((diff < 1) or (diff > 3)) else True
                #
                # check direction with "increasing"
                #
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
