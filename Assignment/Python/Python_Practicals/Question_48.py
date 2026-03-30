# Write a Python script to sort (ascending and descending) a
# dictionary by value.

dict_1 = {"Krunal": 85, "Netra": 88, "Bhavesh": 76}

# Ascending
ascending = dict(sorted(dict_1.items(), key=lambda x: x[1]))
print("Assending order ", ascending)

# Descending
descending = dict(sorted(dict_1.items(), key=lambda x: x[1], reverse=True))
print("Descending order ", descending)
