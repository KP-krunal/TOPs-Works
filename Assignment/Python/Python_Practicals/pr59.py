# Write a program to accepts a list of integers 
# and returns a tuple with the sum of 
# all positive numbers and the sum of all negative numbers

lst = [1, -2, 3, -4, 5, -6]

positive_sum = sum(num for num in lst if num > 0)
negative_sum = sum(num for num in lst if num < 0)


print((positive_sum, negative_sum))
