# Write a Python function that takes a list and returns a new list 
# with unique elements of the first list.

lst_1 = [1,2,3,4,5,4,11,3,6,7]

print(lst_1)
unique_list = []

for i in lst_1:
    if i not in unique_list:
        unique_list.append(i)
    
print(unique_list)
