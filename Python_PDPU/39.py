# Programmer- Parth Sood
# ROll no.- 21BCP252
stri= input("Enter a string:")

for i in stri:
    if i=='.' and stri[i-1].isdecimal() and stri[i+1].isdecimal():
        print("This is a float number:")
    else:
        print("This is not a float number:")
        
 