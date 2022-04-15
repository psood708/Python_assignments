#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b1 = []
for i in range(a):
    n = input("Enter the value for element: ")
    b.append(n)
v = int(input("Enter the number of element you want in a list:"))
b1 = []
for i in range(v):
    m = input("Enter the value:")
    b1.append(m)
print("This is list1:",b)
print("This is list2:",b1)
for j in b1:
    b.append(j)
print("This is combined list:",b)