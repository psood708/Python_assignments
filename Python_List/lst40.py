#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []

for i in range(a):
    we = input("Enter value:")
    b.append(we)
#first character of word
print(b)
p = 1
while(p>0):
   alpha = input("Enter the starting letter you want to get sort of:")
   for alp in b:
       for i in range(len(alp)):
           if alp[0]==alpha:
               print(alp)
               break
   p = int(input("Enter 0/1:"))
