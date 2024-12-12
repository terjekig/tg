#!/bin/python3
# Mull It Over

from pathlib import Path
import re

def part_one(input_file: Path, regex_patterns: dict) -> int:
    """
    input string has mul(digit,digit) commands, sum the prods
    """
    # grep -oE "mul\([0-9]{1,3}\,[0-9]{1,3}\)" input | grep -oE "[0-9]{1,3}\,[0-9]{1,3}"

    ans = 0
    with open(input_file, "r") as infile:
        content = infile.read()

    to_multiply = ' '.join(re.findall(regex_patterns["mul_pattern"], content))
    to_multiply_strimmed = re.findall(regex_patterns["num_pattern"], to_multiply)

    for values in to_multiply_strimmed:
        A, B = re.split(",", values)
        ans += int(A)*int(B)

    return ans


def part_two(input_file: Path, regex_patterns: dict) -> int:
    """
    do() and don't() enable and disable every valid mul() after them
    """

    ans = 0
    with open(input_file, "r") as infile:
        content = infile.read()

    split_input = re.split(regex_patterns["do_dont_pattern"], content)

    enabled = True
    to_multiply_list = []
    for match in split_input:

        if match == "do()": enabled = True
        elif match == "don't()": enabled = False

        else:
            if enabled:
                to_multiply_list.extend(re.findall(regex_patterns["mul_pattern"], match))

    to_multiply = ' '.join(to_multiply_list)
    to_multiply_strimmed = re.findall(regex_patterns["num_pattern"], to_multiply)

    for values in to_multiply_strimmed:
        a, b = re.split(",", values)
        ans += int(a)*int(b)

    return ans


def solution() -> None:
    """
    Solution for Day 3
    """
    input_path = Path(__file__).parent / "input"

    do_dont_pattern = r"(do\(\)|don't\(\))" # wrapping the string in parentheses for .split returns the matched string as well
    mul_pattern = r'mul\([0-9]{1,3},[0-9]{1,3}\)'
    num_pattern = r'[0-9]{1,3},[0-9]{1,3}'

    regex_patterns = {
        "do_dont_pattern" : do_dont_pattern,
        "mul_pattern"     : mul_pattern,
        "num_pattern"     : num_pattern
    }

    solution_1 = part_one(input_path, regex_patterns)
    solution_2 = part_two(input_path, regex_patterns)

    print(f"Solution 1: {solution_1}")
    print(f"Solution 2: {solution_2}")


solution()
