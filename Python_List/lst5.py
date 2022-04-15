#Programmer- Parth Sood
#Roll No.- 21BCP252
a = int(input("enter the number of elements you want:"))
lst=[]
count = 0
for i in range(a):
   b = input("Enter the value:")
   if len(b)>2:
     lst.append(b)
     if b[0]==b[len(b)-1]:
         count+=1
   else:
       print("Invalid entry")
       continue
print(lst)
print("The number of elements satisfying the condition:",count)