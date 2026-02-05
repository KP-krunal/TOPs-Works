#Write a Python program to find whether a given number is even 
#or odd, print out an appropriate message to the use

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even")
else:
    print(f"The number {num} is odd")