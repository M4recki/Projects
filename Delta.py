import math

# Data input
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Mathematical operations


def delta(x, y, z):
    return y**2+(-4)*x*z
# ▲ = b²*(-4)*a*c


def deltaSqrt():
    return math.sqrt(delta(a, b, c))
# √▲


def x1(x, y):
    return ((-y)-deltaSqrt())/(2*x)
# x1 = (-b-√▲)/2*a


def x2(x, y):
    return ((-y)+deltaSqrt())/(2*x)
# x2 = (-b+√▲)/2*a


def x0(x, y):
    return (-y)/(2*x)
#x0 = -b/2*a


print("Delta is: ", delta(a, b, c))
if delta(a, b, c) > 0 or delta(a, b, c) == 0:
    print("Square of the delta is: ", deltaSqrt())
else:
    print("There is no square root of a negative number")
# Presentation of the delta root results

if delta(a, b, c) > 0:
    print("x1 is: ", x1(a, b))
    print("x2 is: ", x2(a, b))
elif delta(a, b, c) == 0:
    print("x0 is: ", x0(a, b))
else:
    print(delta(a, b, c), "is < 0. No solutions")
# Showing the results of the calculations x1 x2 or x0 depending on the results from the previous lines of the program
