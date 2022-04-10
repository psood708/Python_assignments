# Programmer- Parth Sood
# ROll no.- 21BCP252
a = int(input("Enter the number you want to check:"))
sum = 0
while sum==0:
    b = int(input("Enter number to divide"))
    v = b%a
    if v==0:
        print("Your number is divisible by",a)
    else:
        print("Do you want to continue??")
        sum = int(input())
 