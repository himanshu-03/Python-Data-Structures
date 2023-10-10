#Enter the elemts of the list
import sys
l=[]
n = int(input("enter the elements of the list"))
for i in range(n):
    element = str(input("enter the element"))
    l.append(element)

#Finding element
a = str(input("enter the element to be found"))
for i in range(len(l)-1):
    if l[i] == a:
        print("Element found")
        sys.exit(0)
print("The element doesn't exist")



