#Programmer- Parth Sood
#Roll No.- 21BCP252
a = int(input("Enter the number of element you want in a list:"))
b = []
same=[]

a1 = int(input("Enter the number of element you want in a list:"))
b1 =[]
for i in range(a):
    v = input("Enter a value for 1:")
    b.append(v)
for j in range(a1):
    v1 = input("Enter a value for 2:")
    b1.append(v1)
for k in b:
    if k in b1:
       same.append(k) 
print("The same elements are:",same)