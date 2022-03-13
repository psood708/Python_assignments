#Name- Parth Sood
#Objective- To input angles of triangele and check if triangle is legit

a1 = int(input("Enter the angle 1 "))
a2 = int(input("Enter the angle 2 "))
a3 = int(input("Enter the angle 3 "))
if a1+a2+a3==180:
    print("The triangle is legitimate")
else:
    print("The triangle is not legitimate")