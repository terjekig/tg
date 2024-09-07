#!/bin/python3


class Solution:

    def __init__(self) -> None:
        self.roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

    def romanToInt(self, s: str) -> int:

        ans = 0
        for i, char in enumerate(s):
            # print(f"{i} -  Roman {char} in int is {self.roman_dict[char]}")
            if i < len(s)-1 and self.roman_dict[ s[i+1] ] > self.roman_dict[char]:
                ans -= self.roman_dict[char]
            else:
                ans += self.roman_dict[char]
        return ans


solution = Solution()

test_input = "MXLIV"
print(solution.romanToInt(test_input))