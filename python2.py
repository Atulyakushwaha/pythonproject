import random
maxline=3
max_bet=100
min_bet=1
ROW=3
COLS=3

symbol_count={
   "A":2,
   "B":4,
   "C":6,
   "D":8
   }
def get_slot_machine_spin(rows,cols,symbols):
   all_symbols=[]
   for symbol ,symbol_count in symbols.items():
      for _ in range(symbol_count):
         all_symbols.append(symbol)
   columns=[]
   for cols in range(cols):
      cols=[]
      current_symbols=all_symbols[:]
      for cols in range(rows):
         value=random.choice(all_symbols)
         current_symbols.remove(value)
         columns.append(value)
      columns.append(columns)
   return columns

def print_slot_machine(columns):
   for row in range(len(columns[0])):
      for i ,columns in enumerate(columns):
         if i !=len(columns)-1:
            print(columns[row],end=" | ")
         else:
            print(columns[row],end="")
      print("\n")      


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
          print(maxline)
          if line>=1 & line <= maxline:
             break
          else:
             print("Enter a valid no of lines")
        else:
           print("please enter the number")
   return line

def get_bet():
   while True:
        amount=input("what could you like to bet? Rs " )
        if amount.isdigit() :
          amount =  int(amount)
          print(f"{amount}, {max_bet} ,{min_bet}")
          if max_bet>=amount & amount >=min_bet:
             break
          else:
             print(f"Amount must between ${max_bet} - ${min_bet}. ")
        else:
           print("please enter the number")
   return amount



def main() :
   balance=deposit()
   lines=get_number_of_line()
   bet=get_bet()
   
   while True:
      total_bet=bet*lines
      if total_bet > balance:
         print(f"you do not have enough to bet")
        
      else:
        break
   
   print(f"you are betting ${bet} on {lines} lines.Total bet is equal to ${total_bet}")
   slots = get_slot_machine_spin(ROW,COLS,symbol_count)
   print_slot_machine(slots)
   
   print(balance,lines)


main()