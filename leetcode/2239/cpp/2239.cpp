#include <iostream>

#include <stdlib.h>
#include <time.h> 

#include <vector>
#include <cmath>

int main()
{
    std::cout << "Rand init" << std::endl;
    srand(time(0));

    int n_lower = 1;
    int n_upper = 1000;
    int n = rand() % (n_upper - n_lower) + n_lower;
    std::cout << "Generating " << n << " numbers" << std::endl;

    int val_lower = pow(-10,5);
    int val_upper = pow(10,5);

    std::vector<int>numbers;
    for (int i = 1; i <= n; i++){
        int val = ( rand() % (abs(val_lower) + abs(val_upper))  ) - abs(val_lower);
        numbers.push_back(val);
    }


    int current_closest = val_upper + 1;

    for (int i = 0; i < numbers.size(); i++){
        if ( (0 - abs(numbers[i])) > (0 - abs(current_closest)) ){
            current_closest = numbers[i];
        } else if ( abs(numbers[i]) == abs(current_closest) ){
            current_closest = std::max(numbers[i], current_closest);
        }
    }

    std::cout << "The closest number from the array is " << current_closest << std::endl;

}