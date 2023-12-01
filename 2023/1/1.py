#!/usr/bin/python3.10

import re

# --- Day 1: Trebuchet?! ---


test_cali_text = ["1abc2",
    "pqr3stu8vwx",
    "a1b2c3d4e5f",
    "treb7uchet"]

res = []
cali_sum=0
for line in test_cali_text:
    res = re.findall('\d+', line)
    cali_val=int(res[0]+res[-1])
    cali_sum+=cali_val

print(cali_sum)