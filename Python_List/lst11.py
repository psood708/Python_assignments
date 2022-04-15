#Programmer- Parth Sood
#Roll No.- 21BCP252
a = int(input("Enter the number of element you want in a list:"))
b1 = []
b2 = [] 
for i in range(a):
    v = input("Enter element for list 1:")
    n = input("Enter element for list 2:")
    b1.append(v)
    b2.append(n)
print(b1,b2,end='\n')
for m in range(a):
    for p in range(a):
        if b1[m]==b2[p]:
            print("The common element:",b1[m])
