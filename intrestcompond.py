# python compound intrest calcution
import math
principal=0
rate=0
time=0
while True:
    principal=float(input("enter the Prrincipal amount"))
    if principal<=0:
        print("principal can not zero")
    else:
        break

while True:
    rate=float(input("enter the rate amount"))
    if rate<0:
        print("rate can not zero")
    else:
        break
while True:
    time=float(input("enter the time in hour"))
    if time<0:
        print("time can not zero")
    else:
        break
 
compound = principal*pow((1+rate/100 ),time)
print(f"{compound}")
