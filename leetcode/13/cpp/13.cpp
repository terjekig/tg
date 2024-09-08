#include <iostream>
#include <string>
#include <stdlib.h>
#include <map>

class Solution {
public:

    std::map<char, int> roman_nums;

    Solution(){
    roman_nums['I'] = 1;
    roman_nums['V'] = 5;
    roman_nums['X'] = 10;
    roman_nums['L'] = 50;
    roman_nums['C'] = 100;
    roman_nums['D'] = 500;
    roman_nums['M'] = 1000;
    }

    int romanToInt(std::string s) {
        
        int ans = 0;
        char prev_char = 'M'; // previous value would always be smaller than current if I set this to empty
        // greatest val that can be placed before a number to subtract is C, so M is valid to use

        for (int i = 0; i < s.length(); i++){

            // to improve readability
            int prev_val = roman_nums[prev_char];
            int curr_val = roman_nums[s[i]];

            if (prev_val < curr_val){
                ans -= prev_val;
                ans += (curr_val - prev_val);
            } else{
                ans += curr_val;
            }
            
            // shorthand solution in a single line:
            // ans += (prev_val < curr_val) ? (curr_val - 2 * prev_val) : curr_val;

            prev_char = s[i];

        }

        return ans;
    }
};

int main(){

    Solution solution;
    std::string input_str = "MCMXCIV";
    int ans = solution.romanToInt(input_str);
    std::cout << "Roman " << input_str << " in int is " << ans << std::endl;

    return 0;
}