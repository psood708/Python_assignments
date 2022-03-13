#Name- Parth Sood
#Objective- To input all sides of triangle is equilateral,isosceles or scalene triangle

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a==b==c:
    print("The triangle is equilateral")
elif a==b or b==c or c==a:
    print("The triangle is isosceles")
else:
    print("The triangle is scalene")
