#Name- Parth Sood
#Objective- To check if a character is an alphabet,digit or special character

a = input("Enter a character: ")
if (a>='a' or a>='A') and (a<='z' or a<='Z'):
    print("the character is an akphabet")
elif a>='0' and a<='9':
    print("the character is a digit")
else:
    print("The character is a special character")