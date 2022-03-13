#Name- Parth Sood
#Objective- To WAP to calculate loss and profit

a = int((input("Enter total sales amount ")))
b = int(input("Enter total invested amount "))

if b<a:
    print("Congrats you have a profitable business")
    print("Net profit:- ",a-b)

elif b>a:
    print("Ohh Noo Your business is at a loss")
    print("Net Loss:- ",b-a)
else:
    print("There is no profit or loss in your business")
