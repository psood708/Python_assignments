#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
b_num=[]
b_copy=[]

for i in range(a):
    n = int(input("Enter the value for element: "))
    b.append(n)
for k in range(a):
    count =0
    for l in range(a):
    
        if b[k]==b[l]:
            count+=1
    b_num.append(count)
print(b)
print(b_num)