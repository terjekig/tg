#!/bin/python3
# Historian Hysteria

from pathlib import Path

def process_input(path: Path) -> list:
    '''
    I've pasted my puzzle's input to this input file, I need a list of ints
    '''
    
    input_list = []

    with open(path, "r") as infile:
        for line in infile:
             for element in line.strip().split():
                  input_list.append(int(element))
        # or with nested list comprehension
        # input_list = [int(element) for line in infile for element in line.strip().split()]

    return input_list

def main():

    input_data = process_input(Path(__file__).parent / "input") # ./input

    first_column = sorted(input_data[::2])
    second_column = sorted(input_data[1::2])

    dist = [abs(first - second) for first,second in zip(first_column,second_column)]
    print(f"{sum(dist)}")

main()
