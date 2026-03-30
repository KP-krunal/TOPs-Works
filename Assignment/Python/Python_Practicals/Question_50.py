# Write a Python script to check if a given key already exists 
# in a dictionary.

dict_1 = {"name" : "Krunal", "age" : 20, "city" : "Ahmedabad"}

key = "age"

if key in dict_1:
    print("Key exists in the dictionary")
else:
    print("Key does not exist in the dictionary")
