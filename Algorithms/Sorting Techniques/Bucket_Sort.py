def Insertion_Sort(array):
    n = len(array)
    for i in range(1,n):
        for j in range(i,0,-1):
            if(array[j] < array[j-1]):
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array
                

def bucket_sort(array):
    bucket_array = []
    slot_number = 10
    for i in range(slot_number):
        bucket_array.append([])
        
    for j in array:
        index_bucket = int(slot_number*j)
        bucket_array[index_bucket].append(j)
    
    for i in range(slot_number):
        bucket_array[i] = Insertion_Sort(bucket_array[i])
        
    k = 0
    for i in range(slot_number):
        for j in range(len(bucket_array[i])):
            array[k] = bucket_array[i][j]
            k += 1
    
    return array