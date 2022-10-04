choice=int(input("Hi! Select the appropriate option from the given: \n\
1) Area of ​​the rectangle \n\
2) Area of ​​the square \n\
3) Area of ​​a triangle \n\
4) Trapezoid field \n\
5) Circle area \n"))
number1, number2=int(input("Please enter the numbers: \n")).split() 
if choice== 1:
    def Rectangle(a,b):
        return a*b
    print("The area of ​​the rectangle is: ", Rectangle(3,6))
elif choice==2:
    def Square(c):
        return c**2
    print("The area of ​​the square is: ", Square(10))
elif choice==3:
    def Triangle(d,e):
        return (d/2)*e
    print("The area of ​​the triangle is: ", Triangle(3, 7))
elif choice==4:
    def Trapezoid(f,g,h):
        return (((f+g)*h)/2)
    print("The area of ​​the trapezoid is: ", Trapezoid(3, 9, 8))
elif choice==5:
    def Circle(i):
        return (3.14*i**2)
    print("The area of ​​the circle is: ", Circle(6))
else:
    print("Please select the correct option again!")

