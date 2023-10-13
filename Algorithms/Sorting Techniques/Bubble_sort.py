#Bubble Sort is a simple comparison-based sorting algorithm. It repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
#This process continues until no swaps are needed, indicating the list is sorted.
#The algorithm iterates through the list for 'n' elements (length of the list).
#Within each iteration, it compares adjacent elements from the beginning of the list to the (n - i - 1)-th element.
#If an element is greater than the one next to it, a swap is performed.
#This process is repeated until the largest unsorted element "bubbles up" to its correct position at the end of the list.
#The next iteration is then performed on the remaining unsorted portion.
#The process repeats until no more swaps are needed, indicating the list is sorted.
#It has a time complexity of O(n^2) in the worst case, making it impractical for large datasets.

def bubble_sort(arr):
    """
    Sort a list using Bubble Sort.

    >>> bubble_sort([4, 2, 7, 1, 9, 3])
    [1, 2, 3, 4, 7, 9]

    >>> bubble_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
