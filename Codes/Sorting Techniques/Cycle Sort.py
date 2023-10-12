def cycleSort(arr):
    for idx in range(0,len(arr)-1):
        cur_ele = arr[idx]
        pos = idx

        # Find the pos where the element should be inserted
        for j in range(idx+1,len(arr)):
            if arr[j] < cur_ele:
                pos += 1

        # If element is in correct position then move to next cycle
        if idx == pos:
            continue

        # Finding the exact positions if any duplicates
        while cur_ele == arr[pos]:
            pos+=1

        # Put the element to it's other position by swapping
        arr[pos], cur_ele = cur_ele, arr[pos]

        # Traverse through rest of the cycle to rotate
        while pos != idx:
            pos = idx

            # Find the pos to insert
            for k in range(idx+1,len(arr)):
                if arr[k] < cur_ele:
                    pos += 1

            # To check out for duplicates
            while cur_ele == arr[pos]:
                pos += 1

            arr[pos], cur_ele = cur_ele, arr[pos]

n=int(input("Enter the size of array to be sorted\n"))
arr = []
for i in range(0,n):
    arr.append(int(input()))
cycleSort(arr)
print("Sorted Array is")
print(arr)
