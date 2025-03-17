print("Welcome to our restaurent.here's the menu")
print("Pizza: Rs40")
print("Pasta: Rs50")
print("Burger: Rs60")
print("Salad: Rs70")
print("Coffee: Rs80")
order ={'pizza':40,
        'pasta':50,
        'barger':60,
        'salad':70,
        'coffee':80
     }


total=0
def check(m , price) :
  for b in order :
     if m == b :
          price+=order[b]
          return price
     else : print("Item order not founde: plzz try Again...")    

item1 =input("Enter your name of first item:").lower()
total=check(item1 , total)
print(f"your item {item1} is been added to order.") 
print(total) 
c =input("you want to order some thing else:yes or no    ").lower()  
if c == 'yes':
        item2 =input("Enter your name of next item:").lower()
        total=check(item2 , total)
        print(f"your item {item2} is been added to order") 
        print(total)
else : 
     print("thanks for shoping from this shit")


