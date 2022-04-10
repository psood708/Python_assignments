# Programmer- Parth Sood
# ROll no.- 21BCP252
a = int(input("Enter starting point:"))
b = int(input("Enter ending point:"))
numbers=[]
for num in range(a,b+1):
    c = 0
    for i in range(1,num+1):
      if num%i==0:
        c+=1
    if c==2:
        numbers.append(num)
print(numbers)