#Programmer- ParthSood
#Roll no.- 21BCP252
b1 = int(input("Enter the number of elements in list1:"))
b2 = int(input("Enter the number of elements in list2:"))
lst1=[]
lst2=[]
negate=[]

if b1==b2:
   for i in range(b1):
     v1 = int(input("Enter value for list1: "))
     v2 = int(input("Enter the value for list2: "))
     lst1.append(v1)
     lst2.append(v2)
     negate.append(v1-v2)
   print("The negate list is: ",negate)
else:
    print("Please have same elements in both lists.")