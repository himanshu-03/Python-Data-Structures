"""The Bisection Method:
This method is used to find the roots of a continuous equation 
such that the interval [a, b] is provided by the user.
And, f(a)*f(b) < 0 

for more reference (https://www.geeksforgeeks.org/program-for-bisection-method/)
"""

#the continuous function whose roots are to be found
def f(x: float): 
    return float(x*x*x - x*x + 2)


def bisection(a: float, b: float, error = 0.01):
    if (f(a)*f(b) >= 0):
        print("The interval [a, b] are invalid")
        return
    
    while(abs(b-a) >= error):
        mid = float((a+b)/2)

        if (f(mid) == 0.0):
            print("The value of root is : ", mid)
            return
        elif (f(a)*f(mid) < 0):
            b = mid
            continue
        else:
            a = mid
            continue

    if((a-b) <= error):
        print("The value of root is : ", mid)



print("Enter the intervals [a, b] : ")
x = float(input())
y = float(input())

bisection(x, y)
