# Function to calculate the prefix sum of a list using list comprehension
def calculatePrefixSum(arr):
    prefixSum = [sum(arr[:i + 1]) for i in range(len(arr))]
    return prefixSum

def main():
    # Input the list size
    n = int(input("Enter the size of the list: "))

    if n <= 0:
        print("List size must be a positive integer.")
        return 1  # Exit with an error code

    # Input the elements of the list
    print(f"Enter {n} elements of the list:")
    arr = [int(input()) for _ in range(n)]

    # Calculate the prefix sum
    prefixSum = calculatePrefixSum(arr)

    # Display the prefix sum
    print("Prefix Sum:", prefixSum)

if __name__ == "__main__":
    main()
