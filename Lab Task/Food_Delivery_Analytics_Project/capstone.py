import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def build_data():
    rng = np.random.default_rng(7); n = 200
    df = pd.DataFrame({
        "restaurant_name": rng.choice(["Spice Hub","Urban Bites","Dragon Bowl","Sweet Treats","Food Junction"], n),
        "cuisine_type": rng.choice(["Indian","Chinese","Desserts"], n),
        "order_value": rng.uniform(100,800,n),
        "distance_km": rng.uniform(1,20,n),
        "delivery_time_mins": rng.normal(30,8,n),
        "rating": rng.uniform(1,5,n),
        "discount_pct": rng.uniform(0,30,n)
    })
    for col in ["delivery_time_mins","rating"]:
        idx = rng.choice(df.index, 10, replace=False)
        df.loc[idx,col] = np.nan
        df[col] = df[col].fillna(df[col].median())
    df["delivery_speed_kmph"] = df["distance_km"]/(df["delivery_time_mins"]/60)
    df["speed_band"] = pd.qcut(df["delivery_speed_kmph"], 3, labels=["Slow","Normal","Fast"])
    return df

def summary(df):
    print(df.describe().round(2).to_string())

def distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["delivery_time_mins"], bins=15, kde=True)
    plt.title("Delivery Time Distribution"); plt.tight_layout()
    plt.savefig("outputs/delivery_time_distribution.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved outputs/delivery_time_distribution.png")

def heatmap(df):
    plt.figure(figsize=(9,7))
    sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, fmt=".2f",
                cmap="coolwarm", center=0)
    plt.title("Correlation Heatmap"); plt.tight_layout()
    plt.savefig("outputs/capstone_correlation_heatmap.png", dpi=150, bbox_inches="tight")
    plt.close()
    print("Saved outputs/capstone_correlation_heatmap.png")

def restaurant_report(df):
    report = (df.groupby("restaurant_name")
        .agg(mean_order_value=("order_value","mean"),
             mean_delivery_time=("delivery_time_mins","mean"),
             mean_rating=("rating","mean"),
             order_count=("order_value","size"))
        .sort_values("mean_rating", ascending=False))
    print(report.round(2).to_string())

def final_report(df):
    top3 = df.groupby("restaurant_name")["rating"].mean().sort_values(ascending=False).head(3)
    corr = df.select_dtypes(include=np.number).corr().abs()
    np.fill_diagonal(corr.values, np.nan)
    pair = corr.stack().idxmax()
    value = corr.stack().max()
    print("\n=== FINAL SUMMARY ===")
    print("Top 3 restaurants by mean rating:")
    for name, score in top3.items(): print(f"- {name}: {score:.2f}")
    print(f"Highest absolute Pearson correlation: {pair[0]} vs {pair[1]} = {value:.2f}")
    print(f"Mean delivery time: {df.delivery_time_mins.mean():.2f} minutes")
    print(f"Std deviation: {df.delivery_time_mins.std():.2f} minutes")

def main():
    df = build_data()
    while True:
        print("\n1. Summary Statistics\n2. Distribution Analysis\n3. Correlation Heatmap\n4. Restaurant Performance Report\n5. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1": summary(df)
        elif choice == "2": distribution(df)
        elif choice == "3": heatmap(df)
        elif choice == "4": restaurant_report(df)
        elif choice == "5":
            final_report(df); break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
