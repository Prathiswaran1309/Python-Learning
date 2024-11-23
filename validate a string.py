print ("String contain specific word or not")
text = input("Enter a word: ")
word = "python"
word1 = word.title()
if text in word or word1:
    print ("The string contain the word python.")
else:
    print ("The string does not contain the word python.")

