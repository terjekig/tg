#include <iostream>
#include <vector>

class Solution
{
public:
    std::vector<int> twoSum(std::vector<int> &nums, int target)
    {
        int n = nums.size();

        if (n < 2)
        {
            // I know there must be a valid solution, wanted to learn about basic error-handling
            std::cerr << "Not enough digits" << std::endl;
            std::exit(EXIT_FAILURE);
            // or
            throw std::invalid_argument("Not enough digits");
        }


        for (auto i = 0; i < n; i++)
        {

            for (auto j = i + 1; j < n; j++)
            {

                if (nums[i] + nums[j] == target)
                {
                    return {i, j};
                }
            }
        }

        std::cerr << "No solution found, check input" << std::endl;
        std::exit(EXIT_FAILURE);
        // or
        throw std::runtime_error("No solution found, check input");

    }
};

int main() {

    Solution solution;

    std::vector<int> nums = {2,7,11,15};
    int target = 9;

    // try-catch for the throws
    try {
        std::vector<int> result = solution.twoSum(nums, target);
        std::cout << "[" << result[0] << "," << result[1] << "]" << std::endl;
    } catch (const std::exception&e){
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}