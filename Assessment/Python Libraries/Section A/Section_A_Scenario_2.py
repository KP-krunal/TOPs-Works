# Section A
# SCENARIO 2

# You are working on a reporting pipeline for a food delivery platform. 
# You have a Pandas DataFrame with 
# columns: order_id, restaurant_name, city, order_value,
# delivery_time_mins, and rating. A colleague proposes 
# filtering the DataFrame in a for-loop once per restaurant and 
# computing averages manually inside the loop.


# Why should we use groupby() with agg() instead of a for-loop?
# - groupby() with agg() is better than using a Python for-loop 
#   because it groups the data and calculates all the required 
#   averages in a single operation. 
# - It is faster, uses less code, and is easier to read and maintain. 
#   


# What does the DataFrame's index represent after using groupby()?
# - The DataFrame index represents the restaurant names, 
#   so each row in the result corresponds to one restaurant.




import pandas as pd

data = {
    "order_id": [101,102,103,104,105,106,107,108,109,110,
                 111,112,113,114,115,116,117,118,119,120],

    "restaurant_name": [
        "Pizza Hut","Domino's","McDonald's","KFC","Subway",
        "Pizza Hut","Domino's","McDonald's","KFC","Subway",
        "Pizza Hut","Domino's","McDonald's","KFC","Subway",
        "Pizza Hut","Domino's","McDonald's","KFC","Subway"
    ],

    "city": [
        "Ahmedabad","Surat","Rajkot","Ahmedabad","Vadodara",
        "Ahmedabad","Surat","Rajkot","Ahmedabad","Vadodara",
        "Ahmedabad","Surat","Rajkot","Ahmedabad","Vadodara",
        "Ahmedabad","Surat","Rajkot","Ahmedabad","Vadodara"
    ],

    "order_value": [
        450,300,250,550,200,
        600,450,350,700,300,
        500,380,280,650,260,
        550,420,320,750,280
    ],

    "delivery_time_mins": [
        30,25,20,35,18,
        40,30,22,45,20,
        32,28,21,38,19,
        36,29,24,48,22
    ],

    "rating": [
        4.5,4.2,4.0,4.7,4.1,
        4.8,4.5,4.3,4.9,4.2,
        4.6,4.4,4.1,4.8,4.0,
        4.7,4.5,4.2,5.0,4.3
    ]
}

df = pd.DataFrame(data)

# print(df)


# What code (method chain) would you write?
grouped_df = df.groupby('restaurant_name').agg({
    'order_value': 'mean',
    'delivery_time_mins': 'mean',
    'rating': 'mean'
})

print("Grouped DataFrame with averages for each restaurant:\n",grouped_df)