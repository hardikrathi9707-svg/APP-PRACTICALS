import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# Sample customer churn dataset
data = {
    'Age': [24, 27, 22, 32, 29, 25, 100],
    'MonthlyCharges': [500, 600, 520, 580, 620, 550, 6000],
    'Churn': ['Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'Yes']
}

df = pd.DataFrame(data)

# Display dataset
print(df)

# Descriptive Statistics
print(df.describe())
print("Mean:", df['Age'].mean())
print("Median:", df['Age'].median())
print("Mode:", df['Age'].mode()[0])
print("Standard Deviation:", df['Age'].std())
print("Variance:", df['Age'].var())
print("Minimum:", df['Age'].min())
print("Maximum:", df['Age'].max())

# Visualization
plt.hist(df['Age'], bins=5, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

sns.boxplot(y=df['Age'])
plt.title('Box Plot of Age')
plt.show()

plt.scatter(df['Age'], df['MonthlyCharges'])
plt.title('Age vs Monthly Charges')
plt.xlabel('Age')
plt.ylabel('Monthly Charges')
plt.show()

# Correlation Matrix
df_numeric = df[['Age', 'MonthlyCharges']]
sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Handling Missing Values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df = df.dropna()

# Detecting Outliers
df['Age_zscore'] = zscore(df['Age'])
df['Charges_zscore'] = zscore(df['MonthlyCharges'])

print(df)

# Removing Outliers
df_no_outliers = df[
    (df['Age_zscore'].abs() <= 3) &
    (df['Charges_zscore'].abs() <= 3)
]

print(df_no_outliers)

# Capping Outliers
def cap_values(series):
    upper_limit = series.mean() + 3 * series.std()
    lower_limit = series.mean() - 3 * series.std()
    return series.clip(lower=lower_limit, upper=upper_limit)

df['Age_capped'] = cap_values(df['Age'])
df['Charges_capped'] = cap_values(df['MonthlyCharges'])

print(df)