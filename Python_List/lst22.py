#Programmer- Parth Sood
#Roll No.- 21BCP252

a = int(input("Enter the number of element you want in a list:"))
b = []
for i in range(a):
    n = input("Enter the value for element: ")
    b.append(n)
a_cp = input("Enter the item you want to search:")
for j in b:
    if a_cp not in b:
        print("You have entered the wrong item")
        break
    else:
        num = b.index(a_cp)
        print("The index of the item is",num)
        break