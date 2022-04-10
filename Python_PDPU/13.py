# Programmer- Parth Sood
# ROll no.- 21BCP252
numbers = []
for i in range(3):
    a = int(input("Enter the number "))
    numbers.append(a)
print(numbers)
numbers.sort()
print("This is after sort:")
print(numbers)
print("the largest number is :",numbers[2])