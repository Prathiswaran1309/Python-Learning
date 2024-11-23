print ("BMI Calculator Program")
username=input("Please tell your name\n")
# name=username.capitalize()
weight=float(input("Please tell your weight (in kgs)\n"))
height=float(input("Please tell your height (in m)\n"))
# h=height**2
# BMI=(weight/h)
BMI=round(weight/(height**2))
print(f"{username.capitalize()} BMI value is {BMI}")

