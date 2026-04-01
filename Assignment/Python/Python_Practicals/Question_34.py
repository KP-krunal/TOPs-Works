# Write a Python function that takes two lists and returns true if they
# have at least one common member.

# lst1 = [1, 2, 3, 4, 5,6]
# lst2 = [6, 7, 8, 9, 10]

lst1 = input("Enter the first list : ").split()
lst2 = input("Enter the second list : ").split()
print(lst1)
print(lst2)

found = False

for i in lst1:
    for j in lst2:
        if i == j:
            found = True
            break
    
print(found)
