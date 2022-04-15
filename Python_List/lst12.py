#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
 
for i in range(a):
    v = input("Enter value of element:")
    if i !=0 and i!=4 and i!=5:
        b.append(v)
print(b)