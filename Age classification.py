age = int(input("Please enter your age: "))
if age<0:
    print ("Invalid age! Age cannot be negative")
elif age>120:
    print ("Invalid age! Age seems unrealistic")
else:
    if age in range (0,13):
            print ("You are Child")
    elif age in range (13,20):
            print ("You are Teenager")
    elif age in range (20,65):
            print ("You are Adult")
    elif age>=65:
            print ("You are Senior")

