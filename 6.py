#Name- Parth Sood
#Objective- To check if year is leap or not

a = int(input("Enter the year: "))
if  a%100==0 and a%400==0:
    print(a," is a leap year")

else:
    if a%100 !=0 and a%4==0:
        print(a,"is a leap year")
    else:
      print(a,"is not a leap year")