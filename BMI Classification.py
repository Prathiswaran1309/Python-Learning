print ("BMI Classification")
username = input("Please tell your name: ")
weight = float(input("Enter your weight (in kgs): "))
height = float(input("Enter your height (in m): "))
BMI = round(weight/(height**2),2)
print (f"{username.capitalize()} BMI value is {BMI} and")
if BMI < 18.5:
    print("You are underweight")
elif 18.5<= BMI >25:
    print("You are in a normal weight")
elif 25<= BMI >40:
    print("You are over weight")
else:
    print("You are obese")