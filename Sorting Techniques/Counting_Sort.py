def counting_sort(arr):
    # Find the maximum and minimum values in the input array
    max_val = max(arr)
    min_val = min(arr)

    # Create a counting array with a size equal to the range of values
    count_array = [0] * (max_val - min_val + 1)

    # Count the occurrences of each element in the input array
    for num in arr:
        count_array[num - min_val] += 1

    # Reconstruct the sorted array from the counting array
    sorted_array = []
    for i in range(len(count_array)):
        sorted_array.extend([i + min_val] * count_array[i])

    return sorted_array

try:
    input_str = input("Enter a list of numbers separated by spaces: ")
    arr = list(map(int, input_str.split()))
    
    sorted_arr = counting_sort(arr)
    print("Original array:", arr)
    print("Sorted array:", sorted_arr)
except ValueError:
    print("Please enter valid integers separated by spaces.")
