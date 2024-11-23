print("Word reversal tool")
word = input("Enter a word: ")
reverse =''
for i in word:
    reverse = i + reverse
    #print(i)
    print (reverse)
print (f"The reversal word is {reverse}")
