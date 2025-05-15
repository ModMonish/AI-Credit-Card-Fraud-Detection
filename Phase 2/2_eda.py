# Exploratory Data Analysis
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/processed_data.csv')

# Fraud distribution by hour
plt.figure(figsize=(12,6))
df['Hour'] = df['Time'] % 24
sns.histplot(data=df[df['Class']==1], x='Hour', bins=24)
plt.title('Fraud Transactions by Hour of Day')
plt.savefig('../assets/fraud_by_hour.png')

# Correlation heatmap
plt.figure(figsize=(15,10))
sns.heatmap(df.corr()[['Class']].sort_values('Class'), 
            annot=True, cmap='coolwarm')
plt.title('Feature Correlation with Fraud')
plt.savefig('../assets/correlation_heatmap.png')