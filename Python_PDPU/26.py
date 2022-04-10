# Programmer- Parth Sood
# ROll no.- 21BCP252
fact=[]
a = int(input("Enter a number:"))
for i in range(1,a+1):
    if a%i==0:
       fact.append(i) 
print(fact)