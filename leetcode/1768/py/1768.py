#!/bin/python3


class Solution:

    def __init__(self) -> None:
        self.testword1="cica"
        self.testword2="kutya"

    def mergeAlternately(self, word1: str, word2: str) -> str:

        final = ""
        while not (word1 == "" and word2 == "") :
            if len(word1) > 0:
                final += word1[0]
                word1 = word1[1:]
            if len(word2) > 0:
                final += word2[0]
                word2 = word2[1:]
        return final

solution = Solution()
print(solution.mergeAlternately(solution.testword1, solution.testword2))
