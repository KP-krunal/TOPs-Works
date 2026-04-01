# Write a Python program to count the number of characters
# (character frequency) in a string

string = input("Enter a string: ")

count = 0

for char in string:
    if char != " ":
        count += 1

print("Number of characters in the string:", count)
