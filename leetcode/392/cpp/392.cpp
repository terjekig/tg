#include <iostream>
#include <stdlib.h>
#include <string>


// Iterating over t, stepping s's index if there's a match

class Solution {
public:
    bool isSubsequence(std::string s, std::string t) {
        
        if ( s.length() > t.length() ){ return false; }
        if ( s == ""){ return true; }

        int curr_index = 0;

        for (int i = 0; i < t.length(); i++){
            //std::cout << s[curr_index] << " <---> " << t[i];

            if ( s[curr_index] == t[i] ){
                //std::cout << " ✓" << std::endl;
                
                if( curr_index == s.length()-1 ){
                    // Found
                    return true;
                }
                if ( curr_index < s.length()-1 ){
                    curr_index += 1;
                }
            
            } else {
                //std::cout << " X" << std::endl;
                ;
            }
        }
        return false;
        
    }
};


int main() {
    Solution solution;
    std::string string1 = "abc";
    std::string string2 = "adbdcd";
    std::string ans = "";

    bool result = solution.isSubsequence(string1, string2);

    ans = result ? " is a substring of " : " is not a substring of ";
    std::cout << string1 << ans << string2 << std::endl; 

    return result;
}