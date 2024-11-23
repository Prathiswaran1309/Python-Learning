print("Sum of digits")
num = int(input("Enter a number: "))
sum = 0
#using while loop (if using while loop num = int(input("Enter a number: ")
while num>0:
    sum+=num%10
    print(sum)
    num=num//10
#using for loop (if using for loop num = input("Enter a number:") remove the int because int is not iterable
# for i in num:
#     sum = sum + int(i)
print (f"Sum of digits {sum}")

