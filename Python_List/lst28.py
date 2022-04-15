#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []

for i in range(a):
    n = int(input("Enter the value for element: "))
    b.append(n)
b.sort()
print("The second smallest number is:",b[2])