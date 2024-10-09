#include <iostream>
#include <stdlib.h>
#include <string>



class Solution {
public:
    bool isSubsequence(std::string s, std::string t) {
        bool ans = true;
        return ans;
    }
};


int main() {
    Solution solution;
    std::string string1 = "good";
    std::string string2 = "day";
    bool result = solution.isSubsequence(string1, string2);
    std::cout << "Result: " << result;
    return result;
}