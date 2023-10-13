#The selection_sort function is an in-place comparison-based sorting algorithm.
#It takes an input list `arr` and determines its length `n`.
#It iterates through the list using an outer loop with `i` ranging from 0 to `n-1`.
#Inside the outer loop, it initializes `min_index` to `i`, assuming the current element is the minimum.
#It then uses an inner loop with `j` ranging from `i+1` to `n-1` to find the index of the minimum element in the unsorted part of the list.
#If it finds an element at index `j` that is smaller than the element at `min_index`, it updates `min_index` to `j`.
#After the inner loop completes, it swaps the element at index `i` with the element at `min_index`, effectively moving the minimum element to its correct position in the sorted part of the list.
#It repeats this process for each element in the list until the entire list is sorted.
#The sorted list is returned as the result, and the original list is now sorted in ascending order.

def selection_sort(arr):
    """
    Sort a list using Selection Sort.

    >>> selection_sort([4, 2, 7, 1, 9, 3])
    [1, 2, 3, 4, 7, 9]

    >>> selection_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
