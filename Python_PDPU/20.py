a = int(input("Please Enter the min : "))
b = int(input("\nPlease Enter the max : "))
number = []
for n in range(a, b + 1):
    tot = 0
    Times = 0
           
    tp = n
    while tp > 0:
        Times = Times + 1
        tp = tp // 10

    tp = n
    while tp > 0:
        Rem = tp % 10
        tot = tot + (Rem ** Times)
        tp //= 10
    if n == tot:
        number.append(n)
print(number)