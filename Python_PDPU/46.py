# Programmer- Parth Sood
# ROll no.- 21BCP252
count = 0

stg = input("Enter a string:")
ch_ar=input("Enter the character you want to check occurences:")

for i in stg:
    if i == ch_ar:
        count += 1

print(count)