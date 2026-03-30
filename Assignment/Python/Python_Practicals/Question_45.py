# Write a Python program to unzip a 
# list of tuples into individual lists.

lst_names = ["Krunal","Bhavesh","Netra"]
lst_contact = [1234,45678,7890]

# Zip List Into Tuple
ans = zip(lst_names,lst_contact)
print(ans)

# Unzip List Into Tuple

lst_uzip = [('Krunal', 1234), ('Bhavesh', 45678), ('Netra', 7890)]
lst_Name , lst_Marks = zip(*lst_uzip)
print(lst_Name)
print(lst_Marks)