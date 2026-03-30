# Write a Python program to get unique values from a list.

list1 = [1, 2, 2, 5, 8, 4, 8, 5, 6, 7, 9]

list2 = []

for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)
