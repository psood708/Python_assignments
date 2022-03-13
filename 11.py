#Name- Parth Sood
#Objective- To input month number and print number of days in that month

a = int(input("Enter month number "))
b = [1,3,5,7,8,10,12]
c = [4,6,9,11]
if a in b:
    print("The number of days is 31")
elif a in c:
    print("The number of days is 30")
elif a ==2:
    print("the number of days is either 28/29")
else:
    print("Please check your input")