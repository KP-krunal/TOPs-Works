# Write a Python function that takes two lists and returns true if they
# have at least one common member.

lst1 = [1, 2, 3, 4, 5,6]
lst2 = [6, 7, 8, 9, 10]


for i in lst1:
    for j in lst2:
        if i == j:
            print("True")
            break
    else:
        continue
else:
    print("False")