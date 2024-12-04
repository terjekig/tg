#!/bin/python3
# Red-Nosed Reports

from pathlib import Path


def process_input(path: Path) -> list:
    '''
    I've pasted my puzzle's input to this input file
    '''

    input_list = []

    with open(path, "r") as infile:
        for line in infile:
             for report in line.strip().split("\n"):
                  for level in report.split():
                    input_list.append(int(level)) # TODO lists probably won't be good enough, or use list of lists

    return input_list



def solution() -> None:
    """
    TODO
    """
    input_data = process_input(Path(__file__).parent / "input")

    print(input_data)


solution()
