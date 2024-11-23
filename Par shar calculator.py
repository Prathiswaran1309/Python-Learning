print ("Welcome to the Dine & Divide!!")
bill = int(input("What was the total bill in Rs: "))
tip = int(input("How much tip would you like to give? 10, 12 or 15 ? "))
share = int(input("How many people to share the bill? "))
tip_amount = bill*(tip/100)
Each_person = round((bill+tip_amount)/share,2)
print (f"Each person should pay: {Each_person}")














