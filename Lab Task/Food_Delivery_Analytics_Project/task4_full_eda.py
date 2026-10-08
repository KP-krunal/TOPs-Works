import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(7)
n = 200
df = pd.DataFrame({
    "order_value": rng.uniform(100,800,n),
    "distance_km": rng.uniform(1,20,n),
    "delivery_time_mins": rng.normal(30,8,n),
    "rating": rng.uniform(1,5,n),
    "discount_pct": rng.uniform(0,30,n)
})

for col in ["delivery_time_mins","rating"]:
    idx = rng.choice(df.index, size=10, replace=False)
    df.loc[idx,col] = np.nan
    df[col] = df[col].fillna(df[col].median())

df["delivery_speed_kmph"] = df["distance_km"] / (df["delivery_time_mins"]/60)
df["speed_band"] = pd.qcut(df["delivery_speed_kmph"], 3, labels=["Slow","Normal","Fast"])

corr = df.select_dtypes(include=np.number).corr()
plt.figure(figsize=(9,7))
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
plt.title("Food Delivery Numeric Feature Correlation")
plt.tight_layout()
plt.savefig("outputs/correlation_heatmap.png", dpi=200, bbox_inches="tight")
plt.close()

g = sns.pairplot(df, vars=["order_value","distance_km","delivery_time_mins","rating"],
                 hue="speed_band")
g.fig.suptitle("Food Delivery Pairplot by Speed Band", y=1.02)
g.savefig("outputs/pairplot.png", dpi=200, bbox_inches="tight")
plt.close("all")

df.to_csv("outputs/cleaned_food_delivery_data.csv", index=False)
print("Saved EDA outputs.")
