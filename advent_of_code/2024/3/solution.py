#!/bin/python3
# Mull It Over

from pathlib import Path
import re

def process_input(path: Path) -> list:
    '''
    I've pasted my puzzle's input to this input file, string is fine because I'll just regex
    '''

    input_list = []

    with open(path, "r") as infile:
        for line in infile:
             for element in line.strip().split():
                  input_list.append(int(element))

    return input_list

def part_one(input):

    # grep -oE "mul\([0-9]{1,3}\,[0-9]{1,3}\)" input | grep -oE "[0-9]{1,3}\,[0-9]{1,3}"

    ans = 0

    with open(input, "r") as infile:
        content = infile.read()

    mul_pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    num_pattern = r'[0-9]{1,3},[0-9]{1,3}'

    x = ' '.join(re.findall(mul_pattern, content))
    x = re.findall(num_pattern, x)

    for values in x:
        A, B = re.split(",", values)
        ans += int(A)*int(B)

    return ans


def part_two(input):

    return True


def solution() -> None:
    """
    Solution for Day 3
    """
    #input_data = process_input(Path(__file__).parent / "input")
    solution_1 = part_one(Path(__file__).parent / "input")
    #solution_2 = part_two(input_data)

    print(f"Solution 1: {solution_1}")
    #print(f"Solution 2: {solution_2}")


solution()
