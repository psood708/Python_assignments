#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
for i in range(a):
    n = input("Enter the value for element: ")
    b.append(n)
b1 = int(input("Enter the element that you want: "))
try:
  print("Here is the value at",b1,"element: ",b[b1])
except:
    print("Bro you went out of index LOL!!")