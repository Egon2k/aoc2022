#include <iostream>
#include <list>
#include <fstream>

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

    sumArray.sort();

    std::cout << "Part 1: " << sumArray.back() << std::endl;

    for (int i = 0; i < 3; i++){
        sum3 += sumArray.back();
        sumArray.pop_back();
    }
    
    std::cout << "Part 2: " << sum3 << std::endl;

    return 0;
}