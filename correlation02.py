import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data_frame = pd.read_csv("./heart.csv")

cols = ["blood_pressure", "cholesterol", "heart_rate_max"]
pairs = [("blood_pressure", "cholesterol"),
         ("blood_pressure", "heart_rate_max"),
         ("cholesterol", "heart_rate_max")]

corr_matrix = data_frame[cols].corr()

def describe_correlation(r):
    if r >= 0.7: return "Strong +"
    if r >= 0.3: return "Moderate +"
    if r > 0.0: return "Weak +"
    if r <= -0.7: return "Strong -"
    if r <= -0.3: return "Moderate -"
    if r < 0.0: return "Weak -"
    return "None"

# -------------------------------------------------
# Create ONE big canvas
# -------------------------------------------------
fig, axes = plt.subplots(3, 3, figsize=(18, 14))
fig.suptitle("Heart Data Correlation Dashboard", fontsize=20)

# -------------------------------------------------
# (1) Heatmap
# -------------------------------------------------
sns.heatmap(corr_matrix, annot=True, vmin=-1, vmax=1,
            cmap="coolwarm", square=True, ax=axes[0, 0])
axes[0, 0].set_title("Correlation Heatmap")

# -------------------------------------------------
# (2) Scatter plots with regression + correlation line
# -------------------------------------------------
def scatter_with_lines(ax, df, x_col, y_col):
    x = df[x_col].astype(float)
    y = df[y_col].astype(float)
    r = x.corr(y)

    # regression
    a, b = np.polyfit(x, y, 1)
    x_sorted = np.sort(x.values)
    y_reg = a * x_sorted + b

    # correlation line
    x_z = (x - x.mean()) / x.std()
    y_corr = (r * x_z) * y.std() + y.mean()
    order = np.argsort(x.values)
    y_corr_sorted = y_corr.values[order]

    ax.scatter(x, y, alpha=0.5)
    ax.plot(x_sorted, y_reg, linewidth=2, label="Regression")
    ax.plot(x_sorted, y_corr_sorted, linewidth=2, label="Correlation line")

    ax.set_title(f"{x_col} vs {y_col}\nr={r:.2f} ({describe_correlation(r)})")
    ax.grid(True)
    ax.legend()

scatter_with_lines(axes[0, 1], data_frame, *pairs[0])
scatter_with_lines(axes[0, 2], data_frame, *pairs[1])
scatter_with_lines(axes[1, 0], data_frame, *pairs[2])

# -------------------------------------------------
# (3) Histograms
# -------------------------------------------------
sns.histplot(data_frame[cols[0]], bins=30, kde=True, ax=axes[1, 1])
axes[1, 1].set_title(f"Histogram: {cols[0]}")

sns.histplot(data_frame[cols[1]], bins=30, kde=True, ax=axes[1, 2])
axes[1, 2].set_title(f"Histogram: {cols[1]}")

sns.histplot(data_frame[cols[2]], bins=30, kde=True, ax=axes[2, 0])
axes[2, 0].set_title(f"Histogram: {cols[2]}")

# -------------------------------------------------
# (4) Boxplots
# -------------------------------------------------
sns.boxplot(x=data_frame[cols[0]], ax=axes[2, 1])
axes[2, 1].set_title(f"Boxplot: {cols[0]}")

sns.boxplot(x=data_frame[cols[1]], ax=axes[2, 2])
axes[2, 2].set_title(f"Boxplot: {cols[1]}")

# Hide the unused last cell (bottom-right corner)
axes[2, 2].axis("off")

plt.tight_layout()
plt.show()
