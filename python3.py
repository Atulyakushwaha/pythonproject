operation =input("Enter an operation + - * / %")
num1 = float(input("Enter first number " ))
num2 = float(input("Enter secend number "))
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
else:
     print("The number invalid")
print("The number is",round(result,3))
