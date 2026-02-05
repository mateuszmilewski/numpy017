import pandas as pd
import numpy as np

data_frame = pd.read_csv('./heart.csv')
print(data_frame.head(3))


chol_unique = data_frame.cholesterol.unique()

chdf = data_frame.cholesterol
# print("Cholesterol column description:\n", chdf.describe())

std_dev = chdf.std()
print("Standard deviation of cholesterol:", std_dev)


#manually calculate standard deviation
mean_chol = chdf.mean()
squared_diff = (chdf - mean_chol) ** 2
print("Squared differences from mean:\n", squared_diff.head(3))
n = len(chdf)
manual_std_dev = np.sqrt( (1/(n - 1)) * sum( squared_diff ))
print("Manually calculated standard deviation of cholesterol:", manual_std_dev)


# show on snse plot the cholesterol column with mean and std dev lines
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.plot(chdf, marker='o', linestyle='', markersize=5, label='Cholesterol Values')
plt.axhline(y=mean_chol, color='r', linestyle='--', label='Mean')
plt.axhline(y=mean_chol + std_dev, color='g', linestyle='--', label='Mean + 1 Std Dev')
plt.axhline(y=mean_chol - std_dev, color='b', linestyle='--', label='Mean - 1 Std Dev')
plt.title('Cholesterol Values with Mean and Standard Deviation')
plt.xlabel('Index')
plt.ylabel('Cholesterol')
plt.legend()
plt.show()