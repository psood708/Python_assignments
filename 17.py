#Name- Parth Sood
#Objective- To WAP to calculate  percentage and grade

print("******THE MARKS NEED TO BE OUT OF 100******")
a = int(input("Enter marks for PHYSICS: "))
b = int(input("Enter marks for CHEMISTRY: "))
c = int(input("Enter marks for BIOLOGY: "))
d = int(input("Enter marks for MATHEMATICS: "))
e = int(input("Enter marks for COMPUTER: "))
total = (a+b+c+d+e)/5
if total>=90:
    print("Your Grade for this year is : A ")
    print("Your percentage is : ",total," %")
elif total>=80:
    print("Your Grade for this year is : B ")
    print("Your percentage is : ",total," %")
elif total>=70:
    print("Your Grade for this year is : C ")
    print("Your percentage is : ",total," %")
elif total>=60:
    print("Your Grade for this year is : D ")
    print("Your percentage is : ",total," %")
elif total>=40:
    print("Your Grade for this year is : E ")
    print("Your percentage is : ",total," %")
else:
    print("Your grade for this year is : F ")
    print("Your percentage is : ",total," %")



