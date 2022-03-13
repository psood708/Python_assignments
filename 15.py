#Name- Parth Sood
#Objective- To find the roots of a quadratic eq'n

a = int(input("Enter coefficient a: "))
b = int(input("Enter coefficient b: "))
c = int(input("Enter coefficient c: "))
d = b**2 - 4*a*c

if d>0:
    print("The roots are real")
    e = (-b + d)/(2*a)
    f = (-b -d )/(2*a)
    print("The first root is ",e)
    print("The second root is ",f)
elif d==0:
    print("The roots are equal")
    e = -b/(2*a)
    print("The root is ",e)
else:
    print("The roots are not real")
