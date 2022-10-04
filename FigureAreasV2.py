def Rectangle(a, b):
    return a*b
def Square(a):
    return a**2
def Triangle(a, h):
    return a/2*h
def Trapezoid(a, b, h):
    return ((a+b)*h)/2
def Circle(r):
    return 3.14*r**2
#Functions calculating the area of ​​a given figure

print()
choice=input("Hi! Select the appropriate option from the given: \n\
1) Area of the rectangle \n\
2) Area of ​the square \n\
3) Area of ​​a triangle \n\
4) Trapezoid field \n\
5) Circle area \n")
print()
#Here the user selects the figure

if choice =="1" or choice=="3":
    num1 = float(input("Enter first number: \n"))
    print()
    num2 = float(input("Enter second number: \n"))
    print()
elif choice =="2" or choice=="5":
    num1 = float(input("Enter a number: \n"))
    print()
elif choice =="4":
    num1 = float(input("Enter first number: \n"))
    print()
    num2 = float(input("Enter second number: \n"))
    print()
    num3 = float(input("Enter third number: \n"))
    print()
#Here, the user selects the given number that corresponds to the previous selection

if choice == "1":
    print("The area of ​​the rectangle is: ", Rectangle(num1, num2))
    print()
elif choice == "2":
    print("The area of ​​the square is: ", Square(num1))
    print()
elif choice == "3":
    print("The area of ​​the triangle is: ", Triangle(num1, num2))
    print()
elif choice == "4":
    print("The area of ​​the trapezoid is: ", Trapezoid(num1,num2,num3))
    print()
elif choice == "5":
    print("The area of ​​the circle is: ", Circle(num1))
    print()    
else:
    print("Invalid Input. Please try again.")
#The program displays the field of a given figure