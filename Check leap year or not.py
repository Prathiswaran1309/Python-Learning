print ("Check if a year is a leap year")
year = int(input("Enter a year: "))
if (year%400 == 0) or (year%100 !=0) and (year%4 == 0):
    print (f"You entered year {year} is a leap year")
else:
    print (f"You entered year {year} is not a leap year")