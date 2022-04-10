# Programmer- Parth Sood
# ROll no.- 21BCP252
a = int(input("Enter first number:"))
b = int(input("Enter second"))
def hcf(a, b):
    if(b == 0):
        return a
    else:
        return hcf(b, a % b)

print("The gcd of",a,"&",b,"is" , end="")
print(hcf(a, b))