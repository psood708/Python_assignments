# Programmer- Parth Sood
# ROll no.- 21BCP252
a = int(input("Enter a year:"))
if a%400==0 and a%100==0:
    print( a,"is leap year")
elif a%4==0 and a%100!=0:
    print(a,"is leap year")
else:
    print(a,"is not a leap year")