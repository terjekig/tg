#include <iostream>
#include <stdlib.h>

#include <vector>
#include <cmath>
#include <algorithm> // for max in vector


class Solution {
public:
int maxProfit(std::vector<int>& prices) {
    
    // better solution, no vector to hold potential profits, single for loop

    if (prices.empty()) return 0;
    
    int min_price = prices[0];
    int max_profit = 0;
    
    for (const auto& i: prices) {
        // i will be the actual prices, not indices
        min_price = std::min(min_price, i); // check if there is a better buy-in point
        max_profit = std::max(max_profit, (i - min_price)); // update max profit if current price is better to sell at
    }

    return max_profit;
    
    
    
    // subtract every number from a buying point, get the max from it, push it to a vector, then step one forward, do the same, then get the max from the vector
    std::vector<int> profits = {};

    for (auto i = 0; i < prices.size(); i++) {
        // go over every day
        //std::cout << "Looking at day " << i+1 << ", buying price is " << prices[i] << std::endl;
        
        int available_profit_for_i = 0;

        for(auto j = i+1; j < prices.size(); j++) {
            // get best price for that day
            //std::cout << "Possible profit if selling on day " << j+1 << " is " << prices[j] - prices[i] << std::endl;
            int potential_profit = (prices[j]-prices[i]);
            //available_profit_for_i = ( potential_profit > available_profit_for_i ) ? potential_profit  : available_profit_for_i;            
            available_profit_for_i = std::max(potential_profit, available_profit_for_i);            
        }
        //std::cout << "Best profit for day " << i+1 << " is " << available_profit_for_i << std::endl;
        
        profits.push_back(available_profit_for_i);
        
    }
    
    int max_possible_profit = *std::max_element(profits.begin(), profits.end());

    return max_possible_profit;
    }

};


int main() {
    Solution solution;

    std::vector<int> input = {7, 1, 5, 3, 6, 4};
    int result = solution.maxProfit(input);

    std::cout << "Maximum possible profit is: " << result << std::endl;
    return 0;
}