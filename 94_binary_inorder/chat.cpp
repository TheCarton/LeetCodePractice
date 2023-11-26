#include <iostream>
#include <vector>

int main() {
    // Declare a vector of integers
    std::vector<int> myVector;

    // Add elements to the vector
    myVector.push_back(1);
    myVector.push_back(2);
    myVector.push_back(3);

    // Access elements using index
    std::cout << "Elements in the vector: ";
    for (size_t i = 0; i < myVector.size(); ++i) {
        std::cout << myVector[i] << " ";
    }

    // Or use a range-based for loop (C++11 and later)
    std::cout << "\nElements using range-based for loop: ";
    for (const auto &element : myVector) {
        std::cout << element << " ";
    }

    return 0;
}
