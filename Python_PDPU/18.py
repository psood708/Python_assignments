# Programmer- Parth Sood
# ROll no.- 21BCP252
a = int(input("Enter the term of fibonacci series:"))
count = 0
n,m = 0,1
fibe=[]
if a==1:
    print(m)
elif a==2:
    print(m , m)
elif a>2:
     while count< a:
         fibe.append(n)
         term = n + m
         n = m
         m = term
         count+=1
print(fibe)