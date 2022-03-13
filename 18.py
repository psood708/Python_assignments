a = int(input("Enter your Basic Salary: "))
if a<=10000:
    print("Your House Rent Allowance:",a*0.2)
    print("Your Dearness Allowance:",a*0.8)
elif a<=20000:
    print("Your House Rent Allowance:", a* 0.25)
    print("Your Dearness Allowance:", a* 0.9)
elif a>=20000:
    print("Your House Rent Allowance:", a* 0.3)
    print("Your Dearness Allowance:", a* 0.95)