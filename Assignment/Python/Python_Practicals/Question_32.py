# Write a Python program to remove duplicates from a list.

lst1 = [1,1,2,3,4,4,5,6]
lst2 = []

print("Before Fixing the List")
print(lst1)

for i in lst1:
    if i not in lst2:
        lst2.append(i)
print("After Fixing the List")
print(lst2)
