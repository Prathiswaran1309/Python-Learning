'''Getting the input from user and generate the band'''
print ("Band Generator Program")
username = input("Enter your name:\t")
uname = username.capitalize() #it convert the first letter of the first word in sentence to capital letter
color = input ("Please tell me your favourite colour:\t")
city = input ("Please tell me your living city:\t")
output = city+" "+color
concat = output.title() #it convert the first letter of the each word in sentence to capital letter
print (f'Hello "{uname}", Your Band Name is "{concat}"')
