import math
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
char = str(input("Enter majority, minority, or equal character: "))
#Data input
delta = b**2+(-4)*a*c
#Delta calculation
print("Delta is: ", delta)
if delta>0:
    deltaSqrt = math.sqrt(delta)
    #Square root of delta
    print("The root of the delta is:", deltaSqrt)
    x1=((-b)-deltaSqrt)/2*a
    print("x1 is: ", x1)
    x2=((-b)+deltaSqrt)/2*a
    print("x2 is: ", x2)
    #Find square root of delta then calculate x1 and x2: Variant when root of delta is positive
elif delta==0:
    x0=(-b)/2*a
    print("x0 is: ", x0)
    #Variant when root of delta is 0
else:
    print("x !=0. No solutions.")
    #Variant when root of delta is negative
