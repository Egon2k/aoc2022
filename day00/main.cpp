#include <fstream>
#include <iostream>

int main()
{
    std::ifstream infile("data.txt");
    std::string line;

    while (std::getline(infile, line))
    {
        std::cout << line << std::endl;
    }
    
    return 0;
}