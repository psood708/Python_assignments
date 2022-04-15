#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
sum = 0
for i in range(a):
    v = int(input("Enter value of element:"))
    b.append(v)
    sum = sum+v
print(b)
print("The sum of the elements in the list is:",sum)