print ("Welcome to the Dine & Divide!!")
bill = int(input("What was the total bill in Rs:"))
tip_per =  int(input("How much tip would you like to give? 10,12 or 15?"))
tip = (tip_per*bill)/100
Person = int(input("How many people to share the bill?"))
Each_person = round((bill+tip)/Person,2)
print(f"Each person should pay: {Each_person}")


