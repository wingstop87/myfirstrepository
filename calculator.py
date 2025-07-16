Num1 = float(input("Enter the first number: "))

Num2 = float(input("Enter the second number: "))

print("Choose an operation: +  -  *  /")

operation = input("enter the operation: ")

if operation == "+":
    result = Num1 + Num2
    print("The result is:", result)

elif operation == "-":
    result = Num1 - Num2
    print("The result is:", result)

elif operation == "*":
    result = Num1 * Num2
    print("The result is:", result)   

elif operation == "/":
    result = Num1 / Num2
    print("The result is:", result)   
 
                