"""Sieve Of Eratosthenes:
The sieve of eratosthenes is one of the most efficient way to find all
the prime numbers upto the number `n`

for more reference(https://www.geeksforgeeks.org/sieve-of-eratosthenes/)
"""

#importing `math` module which will be used later
import math

#specify upto where you have to find the prime numbers
n = int(input("Enter the range : ")) 

#`arr` is a boolean list that contains `n+1` `False` entries
arr = [False]*(n+1)

#loop upto the square root of the range `n`
for i in range(2,int(math.sqrt(n))+1):
    if arr[i] == False:
        for j in range(i*i, n+1, i):
            #making the entry `True` for all entries whose index is the multiple
            arr[j] = True

#after the loop exits, all the entry that are prime numbers
#are marked as `False`

#printing all the prime numbers
for i in range(2,n):
    if arr[i+1] == False:
        print(i+1)
