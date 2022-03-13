#Name- Parth Sood
#Objective- To count total number of notes in a given amount

rup = [10,20,50,100,200,500,2000]
a = int(input("Enter the amount: "))
for i in rup:
    print("You will require",a//i," notes of ",i)