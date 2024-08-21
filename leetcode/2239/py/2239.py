#!/bin/python3

import random

class Solution:

    def __init__(self) -> None:
        self.nums = [random.randint(-10**5,10**5) for _ in range(random.randint(1,1000))]
        #print(len(self.nums))
        
    def closest(self, numbers: list) -> int:
        ''' This function returns the closest number to zero from the supplied list'''

        current_closest = 1006

        for num in numbers:
            if ( 0 - abs(num) ) > ( 0 - abs(current_closest) ):
                current_closest = num
            elif( abs(num) == abs(current_closest) ):
                #current_closest = num if num > current_closest else current_closest
                current_closest = max(num,current_closest)
        return current_closest
    
solution_instance = Solution()
print(solution_instance.closest(solution_instance.nums))
