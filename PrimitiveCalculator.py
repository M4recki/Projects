from decimal import DivisionByZero
from socket import AI_ADDRCONFIG


number1=input("Input your 1st number: ")
number2=input("Input your 2nd number: ")
Adding = float(number1) + float(number2)
Subtracing = float(number1) - float(number2)
Multiplying = float(number1) * float(number2)
Dividing = float(number1) / float(number2)
Division = float(number1) % float(number2)
Exponentiation = float(number1) ** float(number2)

print("The result of adding these numbers is: "+str(Adding))
print("The result of subtracting these numbers is: "+str(Subtracing))
print("The result of multiplying these numbers is: "+str(Multiplying))
print("The result of dividing these numbers is: "+str(Dividing))
print("The rest of the division is: "+str(Division))
print("The result of exponentiation these numbers is: "+str(Exponentiation))
