unit= input("is this temperature is celsius or fahrenheit(C/F): ")
temp =float(input("Enter the Temperture"))
if unit.upper()=="C":
    temp=round((9*temp)/5+32,1)
    print(f"the Temperture in fahrenheit is : {temp} F")
elif unit.upper() =="F":
    temp=round((temp-32)*5/9,1)
    print(f"the temperature is celsius is: {temp} C")
else :
    print(f"{unit} is an ivalid of measurement")

