#!/usr/bin/python3.10

import re

# --- Day 1: Trebuchet?! ---

res = []
cali_sum=0

with open('input_1','r') as f:
    for line in f:
        res = re.findall('\d', line)
        cali_val=int(res[0]+res[-1])
        cali_sum+=cali_val
        #print(f"res: {res},  line: {line} result: {cali_val}")

print(cali_sum)
