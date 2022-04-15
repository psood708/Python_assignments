#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
for i in range(a):
    n = (input("Enter the value for element: "))
    b.append(n)
print(b)
for l in range(0,a-1,2):
   p = b[l]
   b[l]=b[l+1]
   b[l+1]=p
print(b)