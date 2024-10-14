#include <vector>
#include <stdlib.h>
#include <iostream>
#include <numeric> // for accumulate
#include <algorithm> // for reverse vector


class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        
        std::vector<int> prod_pre;
        std::vector<int> prod_post;
        std::vector<int> result;

        // I could also initialize the vectors, which would help with multiplication w 0 issues I was having:
        // int n = nums.size();
        // std::vector<int> prod_pre(n,1);

        // O(n) means I can't nest for loops to iterate over
        // No division means I can't just prod every element into a new array, then divide


        // One pass for elements before the index, and one pass for elements after.

        for (int i = 0; i < nums.size(); i++){
            // prod_pre.push_back( std::accumulate(nums.begin(), nums.begin() + i, 1, std::multiplies<int>()) );
            // or for O(n):
            if ( (i == 0) ){
                prod_pre.push_back( 1 );
            } else {
                prod_pre.push_back( nums[i-1] * prod_pre.back() );
            }
        }

        for (int i = nums.size(); i > 0; i--){
            // prod_post.push_back( std::accumulate(nums.rbegin(), nums.rend() - i, 1, std::multiplies<int>()) );
            // or for O(n):
            if ( i == nums.size() ){
                prod_post.push_back( 1 );
            } else {
                prod_post.push_back( nums[i] * prod_post.back() );
            }
        }
        std::reverse(prod_post.begin(), prod_post.end()); // reverse instead of swapping push_back to insert ?is it quicker?

        std::cout << "Prod-pre: ";
        for (auto i: prod_pre){
            std::cout << i << " ";
        }
        std::cout << std::endl;

        std::cout << "Prod-post: ";
        for (auto i: prod_post){
            std::cout << i << " ";
        }
        std::cout << std::endl;
        

        // for (int i = 0; i < nums.size(); i++){
        //     result.push_back( prod_pre[i] * prod_post[i] );
        // }
        //return result;


        // To optimize, I can omit the result vector, and just "reuse" either prod_
        for (int i = 0; i < prod_pre.size(); i++){
            prod_pre[i] *= prod_post[i];
        }

        return prod_pre;
    }
};


int main(){

    Solution solution;

    std::vector<int> input({1, 2, 3, 4});
    std::vector<int> result = solution.productExceptSelf(input);

    std::cout << "Input: ";
    for (auto i: input){
        std::cout << i << " ";
    }
        
    std::cout << std::endl;
    
    std::cout << "Result: ";
    for (auto i: result){
        std::cout << i << " ";
    }

    std::cout << std::endl;

    return 0;

}