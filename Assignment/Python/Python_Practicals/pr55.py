# Write a program to sort a list of strings by their length 
# e.g ['apple', 'banana', 'kiwi', 'orange'] 
# output : ['kiwi', 'apple', 'orange', 'banana']

strings = ['apple', 'banana', 'kiwi', 'orange']
print("Original list of strings:", strings)
sorted_strings = sorted(strings, key=len)
print("Sorted strings by length:", sorted_strings)