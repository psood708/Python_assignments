#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b_copy=[]

for i in range(a):
    n = int(input("Enter the value for element: "))
    b.append(n)
for j in b:
    if j not in b_copy:
        b_copy.append(j)
print("The unique values are:",b_copy)