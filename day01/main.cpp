#include <fstream>
#include <iostream>
#include <string.h>
#include <list>
#include <algorithm>

int main()
{
    std::ifstream infile("data.txt");
    std::string line;
    int sum = 0, sum3 = 0;
    std::list<int> sumArray;

    while (std::getline(infile, line))
    {
        if (line.compare("\r") != 0){
            sum += std::stoi(line);
        }
        else{
            sumArray.push_back(sum);
            sum = 0;
        }
    }

    std::cout << "Part 1: " << *std::max_element(sumArray.begin(), sumArray.end()) << std::endl;

    sumArray.sort();

    for (int i = 0; i < 3; i++){
        sum3 += sumArray.back();
        sumArray.pop_back();
    }
    
    std::cout << "Part 2: " << sum3 << std::endl;

    return 0;
}