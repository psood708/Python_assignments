#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b_copy=[]
for i in range(a):
    v = input("Enter value of element:")
    b.append(v)
for l in b:
    b_copy.append(l)
print(b)
print(b_copy)