# Write a program to remove all items from a list 
# that are less than 5 e.g [12,3,4,5,67,0] output [12,5,67]

numbers = [12, 3, 4, 5, 67, 0]
print("Original list:", numbers)
filtered_numbers = [num for num in numbers if num >= 5]
print("Filtered list:", filtered_numbers)
