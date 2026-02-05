import pandas as pd
import numpy as np

data_frame = pd.read_csv('./heart.csv')
print(data_frame.head(10))


bp = data_frame.blood_pressure.unique()
print("Unique blood pressure values:", bp)
chol = data_frame.cholesterol.unique()
print("Unique cholesterol size:", chol.size)

male_female = data_frame.sex.unique()
print("Unique sex values: ", male_female)

print("data frame shape:", data_frame.shape)
print("Data frame description:\n", data_frame.describe())
print("Data frame info:", data_frame.info())


print("chest pain value counts:\n", data_frame.chest_pain.value_counts())




# Q1 - Q4 Quantiles for cholesterol
q1 = data_frame.cholesterol.quantile(0.25)
q2 = data_frame.cholesterol.quantile(0.50)
q3 = data_frame.cholesterol.quantile(0.75)
q4 = data_frame.cholesterol.quantile(1.0)
print("Q1 for cholesterol:", q1)
print("Q2 for cholesterol:", q2)
print("Q3 for cholesterol:", q3)
print("Q4 for cholesterol:", q4)
# IQR for cholesterol - iqr stands for interquartile range
iqr = q3 - q1
print("IQR for cholesterol:", iqr)

# min and max for cholesterol
min_chol = data_frame.cholesterol.min()
max_chol = data_frame.cholesterol.max()
print("Min cholesterol:", min_chol)
print("Max cholesterol:", max_chol)


array_of_quants = data_frame.cholesterol.quantile([0.25, 0.50, 0.75, 1.0]).to_numpy()
print("Array of quantiles for cholesterol:", array_of_quants)

for quant in array_of_quants:
    print("Quantile value:", quant)

# Iterate through cholesterol column to find values above Q3 + 1.5*IQR
upper_bound = q3 + 1.5 * iqr
print("Upper bound for outliers:", upper_bound)
outliers = data_frame[data_frame.cholesterol > upper_bound]
print("Outliers in cholesterol column:")
print(outliers)

# Iterate through cholesterol column to find values below Q1 - 1.5*IQR
lower_bound = q1 - 1.5 * iqr
print("Lower bound for outliers:", lower_bound)
outliers_below = data_frame[data_frame.cholesterol < lower_bound]
print("Outliers below lower bound:")
print(outliers_below)



import seaborn as sns
import matplotlib.pyplot as plt

plt.figure()
sns.boxplot(x=data_frame.cholesterol)
plt.title("Boxplot of Cholesterol")
plt.xlabel("Cholesterol Levels")

plt.figure()
sns.histplot(data_frame.cholesterol, bins=30, kde=True)
plt.title("Histogram of Cholesterol")
plt.xlabel("Cholesterol Levels")
plt.ylabel("Frequency")

plt.show()
