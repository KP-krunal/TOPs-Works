import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
months = np.array(["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"])
orders = rng.integers(1000, 5001, 12)
revenue = orders * rng.uniform(200, 400, 12)
delivery_times = rng.normal(28, 4, 500)

fig, ax = plt.subplots(1, 3, figsize=(17, 5))

ax[0].plot(months, orders, marker="o")
ax[0].set_title("Monthly Orders"); ax[0].set_xlabel("Month"); ax[0].set_ylabel("Orders")
for m, v in zip(months, orders):
    ax[0].annotate(str(v), (m, v), xytext=(0,7), textcoords="offset points",
                   ha="center", fontsize=8)

bar_colors = ["green" if v > 800000 else "red" for v in revenue]
ax[1].bar(months, revenue, color=bar_colors)
ax[1].axhline(800000, linestyle="--", label="Rs 8,00,000 threshold")
ax[1].set_title("Monthly Revenue"); ax[1].set_xlabel("Month"); ax[1].set_ylabel("Revenue (Rs)")
ax[1].legend(fontsize=8)

ax[2].hist(delivery_times, bins=15)
ax[2].axvline(delivery_times.mean(), linestyle="--", label="Mean")
ax[2].set_title("Delivery Time Distribution")
ax[2].set_xlabel("Minutes"); ax[2].set_ylabel("Frequency"); ax[2].legend()

fig.suptitle("Food Delivery Monthly Performance Dashboard")
plt.tight_layout()
plt.savefig("outputs/food_delivery_dashboard.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved outputs/food_delivery_dashboard.png")
