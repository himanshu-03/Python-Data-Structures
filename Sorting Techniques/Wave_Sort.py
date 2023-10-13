# -*- coding: utf-8 -*-
"""The Wave Sort:
is a type of sorting technique in which the values of the array fluctuates
but in a sorted manner

for more reference(https://www.geeksforgeeks.org/sort-array-wave-form-2/)
"""

def waveSort(arr):

    #first arr is sorted using the built in sort function
    arr.sort()

    #now the wave is introduced in the sorted array
    for x in range(0, len(arr)-1, 2):
        #swap adjacent consecutive numbers from this sorted array
        arr[x], arr[x+1] = arr[x+1], arr[x]


arr = []
size = int(input("Enter the size of the array: "))
#input elements in array
print("Enter the elements: ")
for i in range(size):
    arr.append(int(input()))


print("Before wave sort: ", arr)

#implementing wave sort
waveSort(arr)

#showing the wave sorted array
print("After wave sort:", arr)
