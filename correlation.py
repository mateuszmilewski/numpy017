import pandas as pd
import numpy as np

data_frame = pd.read_csv('./heart.csv')
print(data_frame.head(3))

# make correlation matrix between blood_pressure, cholesterol, max_heart_rate
corr_matrix = data_frame[['blood_pressure', 'cholesterol', 'heart_rate_max']].corr()
print("Correlation matrix:\n", corr_matrix)


# add text description of correlation values
def describe_correlation(corr_value):
    if corr_value > 0.7:
        return "Strong positive correlation"
    elif corr_value > 0.3:
        return "Moderate positive correlation"
    elif corr_value > 0.0:
        return "Weak positive correlation"
    elif corr_value < -0.7:
        return "Strong negative correlation"
    elif corr_value < -0.3:
        return "Moderate negative correlation"
    elif corr_value < 0.0:
        return "Weak negative correlation"
    else:
        return "No correlation"
    
for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2:
            corr_value = corr_matrix.loc[col1, col2]
            description = describe_correlation(corr_value)
            print(f"Correlation between {col1} and {col2}: {corr_value:.2f} ({description})")

# visualize correlation matrix using heatmap
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix Heatmap')
#plt.show()



# add scatter plot between blood_pressure and cholesterol and add regression line and add correlation coefficient / line equation
plt.figure(figsize=(8, 6))
plt.scatter(data_frame.blood_pressure, data_frame.cholesterol, alpha=0.7)

# Calculate regression line
z = np.polyfit(data_frame.blood_pressure, data_frame.cholesterol, 1)
p = np.poly1d(z)
plt.plot(data_frame.blood_pressure, p(data_frame.blood_pressure), "r-", linewidth=2, label=f'Regression: y={z[0]:.2f}x+{z[1]:.2f}')

# Add correlation coefficient
corr_coeff = data_frame['blood_pressure'].corr(data_frame['cholesterol'])
plt.text(0.05, 0.95, f'Correlation: {corr_coeff:.2f}', transform=plt.gca().transAxes, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.title('Scatter Plot of Blood Pressure vs Cholesterol')
plt.xlabel('Blood Pressure')
plt.ylabel('Cholesterol')
plt.legend()
plt.grid(True)
plt.show()

