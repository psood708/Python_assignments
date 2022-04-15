#Programmer- Parth Sood
#Roll No.- 21BCP252

import random


a = int(input("Enter the number of element you want in a list:"))
b = []
for i in range(a):
    v = input("Enter the value for the element:")
    b.append(v)
random.shuffle(b)
print(b)