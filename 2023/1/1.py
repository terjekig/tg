#!/usr/bin/python3.10

import re

# --- Day 1: Trebuchet?! ---

res = []
cali_sum=0

if False:
    with open('input_1','r') as f:
        for line in f:
            res = re.findall('\d', line)
            cali_val=int(res[0]+res[-1])
            cali_sum+=cali_val
            #print(f"res: {res},  line: {line} result: {cali_val}")

print(cali_sum)


# --- Part Two ---

string_test=["two1nine",
"eightwothree",
"abcone2threexyz",
"xtwone3four",
"4nineeightseven2",
"zoneight234",
"7pqrstsixteen"]


help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0'
}


for line in string_test:
    res = re.findall('\d|one|two|three|four|five|six|seven|eight|nine|ten', line)
    if res != []:
        # TODO res[*] conversion if it is a string match
        cali_val=int(res[0]+res[-1])
    else:
        cali_val=0
    cali_sum+=cali_val

print(cali_sum)