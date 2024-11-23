Password = input("Please enter the new password\n")
spl_char = "!@#$%^&*()"
if len(Password)<8:
    print ("Password must be at least 8 characters long")
if not any(char.isupper() for char in Password):
    print ("Upper character is missing in your password")
if not any(char.islower() for char in Password):
    print("Lower character is missing in your password")
if not any(char.isnumeric() for char in Password):
    print("Numeric character is missing in your password")
if not any(char in spl_char for char in Password):
    print("Special character is missing in your password")

if (len(Password)>=8 and
    any(char.isupper() for char in Password) and
    any(char.islower() for char in Password) and
    any(char.isnumeric() for char in Password) and
    any(char in spl_char for char in Password)):
    print ("Your Password is strong")
else:
       print ("Please try again with a valid password")