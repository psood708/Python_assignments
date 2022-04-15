#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b_copy=[] 
for i in range(a):
    n = input("Enter the value for element: ")
    b.append(n)
m = ''.join(b)
print("The integer is",m)