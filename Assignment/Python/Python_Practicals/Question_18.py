# Write a Python program to count occurrences of a substring 
# in a string.

str1 = input("Enter a string: ")
str2 = input("Enter a substring: ")

count = 0

count = str1.count(str2)

print("The substring", str2, "=", count)
