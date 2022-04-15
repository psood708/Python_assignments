#Programmer- Parth Sood
#Roll No.- 21BCP252
a = int(input("Enter the number of element you want in a list:"))
b = []
for i in range(a):
    v = int(input("Enter value of element:"))
    b.append(v)
print(b)
b.sort()
print("The largest element in list is:",b[a-1])