#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
for i in range(a):
    n = input("Enter the character for element: ")
    b.append(n)
nb = ''.join(b)
print(nb)
print(type(nb))