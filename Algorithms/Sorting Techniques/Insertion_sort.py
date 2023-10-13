#Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted list one element at a time.
#The algorithm starts with the second element (index 1) and iterates through the list (of length 'n').
#It selects the current element as the 'key' and compares it with the elements to its left in the sorted portion of the list (elements before the current position).
#The algorithm moves elements in the sorted portion to the right to create space for the 'key' if the 'key' is smaller than the element being compared.
#This process continues until the 'key' is in its correct position in the sorted portion.
#The algorithm repeats this process for each element in the list, gradually expanding the sorted portion from left to right.
#Insertion Sort is efficient for small lists or lists that are already partially sorted.
#It has a time complexity of O(n^2) in the worst case, similar to Bubble and Selection Sort, making it less efficient for large datasets.
#It minimizes the number of comparisons and swaps, making it a suitable choice for small datasets or nearly sorted lists.

def insertion_sort(arr):
    """
    Sort a list using Insertion Sort.

    >>> insertion_sort([4, 2, 7, 1, 9, 3])
    [1, 2, 3, 4, 7, 9]

    >>> insertion_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
