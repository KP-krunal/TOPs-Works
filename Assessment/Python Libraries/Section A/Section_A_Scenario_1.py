# Section A
# SCENARIO 1
# You are building a delivery fee calculator for a food delivery platform. 
# You have a NumPy array of 50,000 order distances (in km) and 
# need to compute a delivery fee for every order simultaneously. 
# A team mate suggests iterating over the array using a Python
# for-loop and appending results to a list.

import numpy as np

# Generate 50,000 random delivery distances between 1 km and 20 km
distances = np.random.uniform(1, 20, 50000)

print("Distances :", distances)


# Calculate delivery fee
fees = distances * 5
print("Fees :", fees)


# 1 Why is NumPy vectorization better than a Python for-loop?
# - Suppose you have 50,000 delivery orders.
# - A Python for-loop calculates the delivery fee one order at a time.
# - This takes more time.

# - NumPy vectorization calculates the delivery fee for all 50,000 
#   orders at the same time.
# - So NumPy vectorization is better because it calculates all values 
#   at once. It is faster and requires less code than 
#   using a Python for-loop.


# 2 What is broadcasting?
# - Broadcasting means NumPy automatically applies one value 
#   (called a scalar), like ₹5, to every element in the array.


# 3 When do we still need a Python for-loop?
# - A Python for-loop is still needed when each item needs different 
#   logic or conditions, such as checking whether a 
#   customer is a VIP before calculating the delivery fee.