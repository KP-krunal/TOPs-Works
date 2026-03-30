# Write a Python program to get a string made of 
# the first 2 and the last 2 chars from a given a string. 
# If the string length is less than 2, return
# instead of the empty string.

sen = input("Enter a string: ")
if len(sen) < 2:
    print("Empty string")
else:
    print(sen[:2] + sen[-2:])
    # print(sen[:2] + sen[-2:])