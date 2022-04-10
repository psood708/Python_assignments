# Programmer- Parth Sood
# ROll no.- 21BCP252
print("Enter all strings in lowercase")
a = input("Enter first string:")
b = input("Enter second string:")
if(len(a) == len(b)):
    sorted_a = sorted(a)
    sorted_str2 = sorted(b)

    if(sorted_a == sorted_str2):
        print(a," and " ,b ," are anagram.")
    else:
        print(a ," and ", b ," are not anagram.")

else:
    print(a," and ",b ," are not anagram.")