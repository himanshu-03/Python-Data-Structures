# Fibonacci searching algorithm only works on the sorted array with time complexity O(log(n)).

# Function to find minimum out of two element
def min(x, y):
    return x if x <= y else y

# Returns the index of x if present, else returns -1
def fibonacciSearch(array, target, n):
    # If target is greater than last element of the array or smaller than first element of the array
    if target > array[n-1] or target < array[0]:
        return -1
    
    # Initialize Fibonacci numbers
    fiboMMm2 = 0  # (m-2)'th Fibonacci No.
    fiboMMm1 = 1  # (m-1)'th Fibonacci No.
    fiboM = fiboMMm2 + fiboMMm1  # m'th Fibonacci

    # fiboM is going to store the smallest Fibonacci Number greater than or equal to n
    while fiboM < n:
        fiboMMm2, fiboMMm1 = fiboMMm1, fiboM
        fiboM = fiboMMm2 + fiboMMm1

    # Marks the eliminated range from the front
    offset = -1

    # While there are elements to be inspected.
    # Note that we compare array[fiboMm2] with target.
    # When fiboM becomes 1, fiboMm2 becomes 0
    while fiboM > 1:
        # Check if fiboMm2 is a valid location
        i = min(offset + fiboMMm2, n - 1)

        # If target is greater than the value at index fiboMm2, cut the subarray array from offset to i
        if array[i] < target:
            fiboM, fiboMMm1, fiboMMm2 = fiboMMm1, fiboMMm2, fiboM - fiboMMm1
            offset = i

        # If target is greater than the value at index fiboMm2, cut the subarray after i+1
        elif array[i] > target:
            fiboM, fiboMMm1, fiboMMm2 = fiboMMm2, fiboMMm1 - fiboMMm2, fiboM - fiboMMm1

        # Element found, return index
        else:
            return i

    # Comparing the last element with target
    if fiboMMm1 and array[offset + 1] == target:
        return offset + 1

    # Element not found, return -1
    return -1

if __name__ == "__main__":
    array = [5, 6, 7, 8, 17, 19, 20, 21, 23, 34, 67, 97, 675]
    n = len(array)
    target = 31
    index = fibonacciSearch(array, target, n)
    if index != -1:
        print(target, "is present at index:", index)
    else:
        print(target, "isn't present in the array")
