operation =input("Enter an operation + - * / %")
num1 = int(input("Enter first number " ))
num2 = int(input("Enter secend number "))
if operation == "+" :
     result=num1+num2
elif operation =="-":
     result= num1-num2
elif operation == "*":
     result = num1 * num2
elif operation == "/":
     result = num1 / num2
elif operation == "%":
     result= num1 % num2
print("The number is", result)
