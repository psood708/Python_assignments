#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b1=[]
 
for i in range(a):
    v = int(input("Enter value of element:"))
    b.append(v)
print(b)
for i in b:
    if i%2==1:
         b1.append(i)
print(b1)