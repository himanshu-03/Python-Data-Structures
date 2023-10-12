# Bucket Sort in Python

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

user_input = input("Enter a list of elements to be sorted, separated by spaces: ")
array = [int(x) for x in user_input.split()]
print("Sorted Array in descending order is")
print(bucketSort(array))
