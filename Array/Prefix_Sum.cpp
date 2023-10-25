#include <iostream>
#include <vector>

// Function to calculate the prefix sum of an array
std::vector<int> calculatePrefixSum(const std::vector<int>& arr) {
    int n = arr.size();
    std::vector<int> prefixSum(n, 0);

    prefixSum[0] = arr[0];
    for (int i = 1; i < n; i++) {
        prefixSum[i] = prefixSum[i - 1] + arr[i];
    }

    return prefixSum;
}

int main() {
    // Input the array size
    int n;
    std::cout << "Enter the size of the array: ";
    std::cin >> n;

    if (n <= 0) {
        std::cout << "Array size must be a positive integer." << std::endl;
        return 1; // Exit with an error code
    }

    // Input the elements of the array
    std::vector<int> arr(n);
    std::cout << "Enter " << n << " elements of the array: ";
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    // Calculate the prefix sum
    std::vector<int> prefixSum = calculatePrefixSum(arr);

    // Display the prefix sum
    std::cout << "Prefix Sum: ";
    for (int i = 0; i < n; i++) {
        std::cout << prefixSum[i] << " ";
    }
    std::cout << std::endl;

    return 0;
}
