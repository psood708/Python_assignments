a = int(input("Enter your total electricity units : "))
if a<=50:
    bill = a*0.5
    print("Your total electrical bill is: ",bill*1.2)
    print("Your surcharge is ",0.2*bill)
elif a<=150:
    bill = (50*0.5)+ ((a-50)*0.75)
    print("Your total electrical bill is:",bill*1.2)
    print("Your surcharge is ", 0.2 * bill)
elif a<=250:
    bill = (50*0.5) + (100*0.75) + ( (a-150)*1.2 )
    print("Your total electrical bill is:",bill*1.2)
    print("Your surcharge is ", 0.2 * bill)
elif a>250:
    bill = (50*0.5) + (100*0.75) + (100*1.2) + ((a-250)*1.5)
    print("Your total electrical bill is:",bill*1.2)
    print("Your surcharge is ", 0.2 * bill)

