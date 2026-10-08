import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
restaurants = ["Spice Hub","Urban Bites","Dragon Bowl","Sweet Treats","Food Junction"]
cities = ["Ahmedabad","Vadodara","Surat"]
cuisines = ["Indian","Chinese","Desserts"]
n = 50

df = pd.DataFrame({
    "restaurant_name": rng.choice(restaurants, n),
    "city": rng.choice(cities, n),
    "order_value": rng.uniform(150, 1200, n).round(2),
    "delivery_time_mins": rng.integers(18, 55, n),
    "rating": rng.uniform(2.8, 5.0, n).round(1),
    "cuisine_type": rng.choice(cuisines, n)
})

summary = (
    df.groupby("restaurant_name")
      .agg(mean_order_value=("order_value","mean"),
           mean_delivery_time=("delivery_time_mins","mean"),
           mean_rating=("rating","mean"))
      .query("mean_rating > 4.0 and mean_delivery_time < 35")
      .sort_values("mean_order_value", ascending=False)
      .reset_index()
)

print("\n=== RESTAURANT PERFORMANCE ===")
print(summary.to_string(index=False, float_format=lambda x: f"{x:.2f}"))
