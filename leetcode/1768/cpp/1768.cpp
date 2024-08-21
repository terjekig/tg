#include <iostream>
#include <stdlib.h>
#include <string>


class Solution {
public:
    std::string mergeAlternately(std::string word1, std::string word2) {

        std::string ans = "";
        int n_iters = std::max(word1.length() , word2.length());

        for (int i = 0; i < n_iters; i++){
            if ( word1.length() > 0){
                ans += word1[0];
                word1.erase(0,1);
            }
            if ( word2.length() > 0){
                ans += word2[0];
                word2.erase(0,1);
            }
        }

        return ans;
    }
};

int main() {
    Solution solution;
    std::string string_1 = "cica";
    std::string string_2 = "kutya";
    std::string result = solution.mergeAlternately(string_1, string_2);
    std::cout << "Result: " << result << std::endl;
    return 0;
}