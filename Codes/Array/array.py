from array import array

int_array = array('i', [1, 2, 3, 4, 5])

print("Integer Array:", int_array)

print("Element at index 0:", int_array[0])
print("Element at index 2:", int_array[2])

int_array[1] = 10
print("Modified Array:", int_array)

int_array.append(6)
int_array.extend([7, 8, 9])
print("Updated Array:", int_array)

int_array.remove(8)
print("Array after removing 8:", int_array)

index = int_array.index(5)
print("Index of 5:", index)

length = len(int_array)
print("Length of the array:", length)

for item in int_array:
    print(item, end=' ')

int_list = int_array.tolist()
print("\nArray converted to a list:", int_list)