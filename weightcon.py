weight= float(input("Enter your weight"))
unit = input("kilograms or pounds? (K or L)")

if unit.upper()=="K":
    weight=weight*2.205
    uni="lbs"
    print(f"your weight is : {round(weight,1)} {uni}")
elif unit.upper()=="L":
    weight=weight*2.20
    uni="k"
    print(f"your weight is : {round(weight,1)} {uni}")
else:
    
    print(f"{unit} was not vaild ")

