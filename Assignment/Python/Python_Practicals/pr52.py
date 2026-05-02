# Write a program to check if a given string is a valid phone number 
# (e.g., str_phone: (123) 456-7890 output True)

str_phone = input("Enter a phone number: ")

if len(str_phone) == 10 and str_phone.isdigit():
    print("True")
else: 
    print("False")
