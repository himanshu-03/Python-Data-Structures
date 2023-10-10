# The function radixsort takes a list of integers as an input.
# The RADIX is set to 10 because we deal with decimal numbers.
# The while loop continues until all digits have been sorted.
# The list of numbers is divided into buckets based on the digit at the current placement.
# The numbers are then collected from the buckets, resulting in a list sorted by the current digit.
# The placement is multiplied by the RADIX, moving on to the next digit.


def radixsort(nums):
    RADIX = 10
    maxLength = False
    tmp , placement = -1, 1

    while not maxLength:
        maxLength = True
        buckets = [list() for _ in range(RADIX)]

        for  i in nums:
            tmp = i // placement
            buckets[tmp % RADIX].append(i)
            if maxLength and tmp > 0:
                maxLength = False

        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                nums[a] = i
                a += 1

        placement *= RADIX
    return nums
