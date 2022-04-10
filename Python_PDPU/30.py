# Programmer- Parth Sood
# ROll no.- 21BCP252
s_tr = input("Enter the string:")
lst = ['A','E','I','O','U','a','e','i','o','u']
vowel=0
for i in lst:
    for j in range(0,len(s_tr)):
        if (i==s_tr[j]):
            vowel+=1
print("The number of vowel in",s_tr,"are",vowel)