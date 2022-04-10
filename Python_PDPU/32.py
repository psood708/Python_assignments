# Programmer- Parth Sood
# ROll no.- 21BCP252
b = [4,1,65,2,6,2,3,86,9,1]
b1=[]
b2=[]
num=int(input("Enter the element you want to slice from:"))
for i in range(0,num+1):
    b1.append(b[i])
for j in range(num+1,len(b)):
        b2.append(b[j])
print("The original list",b)
print("This is first part of slice",b1)
print("This is second part of slice",b2)