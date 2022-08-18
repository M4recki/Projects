import math #Importing the math library to root numbers

num1=float(input("Enter your first number: "))
num2=float(input("Enter your second number: ")) #User selects numbers

print()
print("Adding (+) - 1")
print("Subtraction (-)  - 2")
print("Multiplication (*) - 3")
print("Division (/) - 4")
print("Exponentiation (**) - 5")
print("Extraction of a root (√) - 6") #Description of the operations

print()
choice=input("What kind of operartion would you like to perform? ") #The user selects the operation
print()

if choice=="1":
    print("The result of adding",num1,"and",num2,"is:",num1+num2) #Adding
elif choice=="2":
    print("The result of subtracting",num1,"and",num2,"is:",num1-num2) #Subtraction
elif choice=="3":
    print("The result of multiplying",num1,"and",num2,"is:",num1*num2) #Multiplication
elif choice=="4":
    if num2==0:
        print("We do not divide by 0!") #Remember not to divide by 0 :)
    else:
        print("The result of dividing ",num1,"and",num2,"is:",num1/num2) #Division
        print("The remainder of dividing",num1,"and",num2,"is:",num1%num2) #The remainder of dividing
elif choice=="5":
    print("The result of exponentiation",num1,"and",num2,"is:",num1**num2) #Exponentiation
elif choice=="6":
    print("The result of the square root",num1,"is:",math.sqrt(num1))
    print("The result of the square root",num2,"is:",math.sqrt(num2)) #Extraction of a 2 numbers
else:
    print("Error - invalid character. Please try again.") #Information about the wrong character entered by the user
  

   
