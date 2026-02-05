import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.ion()  # <<< KEY LINE

data_frame = pd.read_csv("./heart.csv")
cols = ["blood_pressure", "cholesterol", "heart_rate_max"]

# -------------------------------------------------
# Heatmap window
# -------------------------------------------------
corr_matrix = data_frame[cols].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, vmin=-1, vmax=1, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show(block=False)

# -------------------------------------------------
# Function for scatter window
# -------------------------------------------------
def scatter_window(x_col, y_col):
    x = data_frame[x_col].astype(float)
    y = data_frame[y_col].astype(float)
    r = x.corr(y)

    a, b = np.polyfit(x, y, 1)
    x_sorted = np.sort(x.values)
    y_reg = a * x_sorted + b

    x_z = (x - x.mean()) / x.std()
    y_corr = (r * x_z) * y.std() + y.mean()
    order = np.argsort(x.values)
    y_corr_sorted = y_corr.values[order]

    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, alpha=0.5)
    plt.plot(x_sorted, y_reg, label="Regression", linewidth=2)
    plt.plot(x_sorted, y_corr_sorted, label=f"Correlation line (r={r:.2f})", linewidth=2)

    plt.title(f"{x_col} vs {y_col}")
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.legend()
    plt.grid(True)
    plt.show(block=False)

# -------------------------------------------------
# Open 3 scatter windows
# -------------------------------------------------
scatter_window("blood_pressure", "cholesterol")
scatter_window("blood_pressure", "heart_rate_max")
scatter_window("cholesterol", "heart_rate_max")

# -------------------------------------------------
# Histograms windows
# -------------------------------------------------
for c in cols:
    plt.figure(figsize=(8, 4))
    sns.histplot(data_frame[c], bins=30, kde=True)
    plt.title(f"Histogram: {c}")
    plt.show(block=False)

# -------------------------------------------------
# Keep script alive until you close figures
# -------------------------------------------------
plt.ioff()
plt.show()
