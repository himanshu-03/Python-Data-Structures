# Jump Search is an efficient searching algorithm for ordered lists. It divides the list into smaller blocks and jumps ahead by fixed steps to quickly reach a block that might contain the target value. It then performs a linear search within that block, providing a balance between the efficiency of binary search and the simplicity of linear search. Jump Search is especially useful for large datasets where binary search might be less efficient due to its logarithmic time complexity.

import math

def jumpSearch(arr, x, n):

    # Finding block size to be jumped
    step = math.sqrt(n)

    # Finding the block where element is
    # present (if it is present)
    prev = 0
    while arr[int(min(step, n)-1)] < x:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1

    # Doing a linear search for x in
    # block beginning with prev.
    while arr[int(prev)] < x:
        prev += 1

        # If we reached next block or end
        # of array, element is not present.
        if prev == min(step, n):
            return -1

    # If element is found
    if arr[int(prev)] == x:
        return prev

    return -1
