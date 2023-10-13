# Merge sort is a highly efficient and stable sorting algorithm 
# that follows the divide-and-conquer approach. It works by repeatedly
# dividing an unsorted list into two halves until individual elements
# are isolated, sorts them, and then merges them back together to form 
# a fully sorted list. 

# For example, consider the list [38, 27, 43, 3, 9, 82, 10]. It's divided into two halves, sorted, and then merged:

# 1. Divide: [38, 27, 43, 3, 9, 82, 10] → [38, 27, 43] and [3, 9, 82, 10]

# 2. Conquer (Sort): Sort the sublists: [27, 38, 43] and [3, 9, 10, 82]

# 3. Merge: Merge the sorted sublists: [27, 38, 43] and [3, 9, 10, 82] → [3, 9, 10, 27, 38, 43, 82]

# Merge sort has a consistent time complexity of O(n log n), making it 
# ideal for large datasets. However, it requires additional memory for 
# merging, which can be a drawback in memory-constrained scenarios.

def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    sorted_array = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])

    return sorted_array