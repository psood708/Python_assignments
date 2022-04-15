#Programmer- Parth Sood
#Roll No.- 21BCP252

from random import randrange


a = int(input("Enter the number of element you want in a list:"))
b = []
m = randrange(0,a+1)
for i in range(a):
    n = input("Enter the value for element: ")
    b.append(n)
print("The randomly selected item is:",b[m])