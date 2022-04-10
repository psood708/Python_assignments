# Programmer- Parth Sood
# ROll no.- 21BCP252
from cmath import sqrt
a = float(input("Enter first coefficient:"))
b = float(input("Enter second coefficient:"))
c = float(input("Enter third coefficient:"))
e = b*b - 4*a*c
print("The Determinant:",sqrt(e))
if e==0:
   print("The roots are equal")
   print("Root is:",-b/(2*a))
elif e<0:
    print("The roots are imaginary")
else:
    print("The roots are real and different")
    print("Root 1 :",(-b + sqrt(e))/(2*a))
    print("Root 2:",(-b-sqrt(e))/(2*a))