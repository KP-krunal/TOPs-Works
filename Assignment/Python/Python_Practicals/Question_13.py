# Write a Python program that will return true if the two given
# integer values are equal or their sum or difference is 5.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 == num2:
    print("True")
elif num1 + num2 == 5: 
    print("True")
elif num1 - num2 == 5:
    print("True")
else:
    print("False")