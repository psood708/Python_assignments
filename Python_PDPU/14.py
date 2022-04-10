# Programmer- Parth Sood
# ROll no.- 21BCP252
a = int(input("Enter a number:"))
c = 0
for i in range(1,a):
    if a%i==0:
        c+=1
if c>1:
   print(a,"is not a prime number")
elif c==1:
    print(a,"is a prime number")
