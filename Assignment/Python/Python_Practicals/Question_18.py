# Write a Python program to count occurrences of a substring 
# in a string.

str1 = input("Enter a string: ")
str2 = input("Enter a substring: ")

count = 0

for i in range(len(str1)):
    if str1[i:i+len(str2)] == str2:
        count += 1

print("The substring", str2, "=", count)