maxline=3
def deposit():
    while True:
        amount=input("what would you want to deposit= Rs ")
        if amount.isdigit() :
          amount =  int(amount)
          if amount>0 :
             break
          else:
             print("amount should be more then 0")
        else:
           print("please enter the number")
    return amount
def get_number_of_line():
   while True:
        line=input("how money line you want to bet(1-"+str(maxline)+")  ")
        if line.isdigit() :
          line =  int(line)
          if line>=1 & line <= maxline:
             break
          else:
             print("Enter a valid no of lines")
        else:
           print("please enter the number")
   return line



def main() :
   balance=deposit()
   lines=get_number_of_line()
   print(balance,lines)

main()