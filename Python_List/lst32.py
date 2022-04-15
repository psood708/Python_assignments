#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b_copy=[]
b_compare=[]
a_sub = int(input("Enter the length of the sublist:"))
for i in range(a):
    n = (input("Enter the value for element: "))
    b.append(n)
for j in range(a_sub):
    k = input("Enter the value:")
    b_copy.append(k)
for k in b:
    for o in b_copy:
        if k==o:
          b_compare.append(k)
print(b)
print(b_copy)
print(b_compare)
b_compare.sort()
b_copy.sort()
if b_copy==b_compare:
    print("The subset is a part of main list")
 