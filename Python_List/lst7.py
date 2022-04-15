#Programmer- Parth Sood
#Roll No.- 21BCP252
a = int(input("Enter the number of elements you want:"))
lst=[]
lstnew=[]
for i in range(a):
    v = input("enter the value:")
    lst.append(v)
for j in lst:
    if j not in lstnew:
        lstnew.append(j)
print("The exclusive list:",lstnew)