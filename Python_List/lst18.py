#Programmer- ParthSood
#Roll no.- 21BCP252
a = int(input("Enter the number of elements you want in list:"))
lst =[]
lst_copy=[]
mega_lst=[]
mega_lst_copy=[]
for i in range(a):
    v = input("Enter value:")
    lst.append(v)
    lst_copy.append(v)
print(lst)
for j in range(a):
    for n in range(a):
        if lst[j]!= lst[n]:
            b = lst[j]
            lst[j]=lst[n]
            lst[n]=b
        
        print(lst,end='  ')
             
 
 
