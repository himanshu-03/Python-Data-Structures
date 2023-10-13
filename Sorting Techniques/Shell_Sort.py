def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Initial gap size

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2  # Reduce the gap size

# Input a list of numbers from the user
user_input = input("Enter a list of numbers separated by spaces: ")
user_list = [int(x) for x in user_input.split()]

# Apply Shell sort to the user's list
shell_sort(user_list)

# Display the sorted list
print("Sorted list:", user_list)
