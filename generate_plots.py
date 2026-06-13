import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

os.makedirs('screenshots', exist_ok=True)
os.makedirs('demo-assets/screenshots', exist_ok=True)

sns.set_theme(style="whitegrid")
plt.rcParams.update({'figure.figsize': (10, 6), 'figure.dpi': 300})

def save_plot(name):
    plt.tight_layout()
    plt.savefig(f'screenshots/{name}.png')
    plt.savefig(f'demo-assets/screenshots/{name}.png')
    plt.close()

print("Generating California Housing visualizations...")
data = fetch_california_housing(as_frame=True)
df = data.frame

plt.figure(figsize=(10, 6))
sns.histplot(df['MedHouseVal'], bins=50, kde=True, color='teal')
plt.title('Distribution of Median House Values ($100,000s)')
plt.xlabel('Median House Value')
plt.ylabel('Count')
save_plot('01-target-distribution')

plt.figure(figsize=(12, 8))
sns.scatterplot(x='Longitude', y='Latitude', data=df, hue='MedHouseVal', palette='viridis', alpha=0.5, s=15)
plt.title('Geographic Distribution of House Prices')
save_plot('02-geographic-distribution')

plt.figure(figsize=(10, 8))
corr = df.corr()
mask = np.triu(np.ones_like(corr, dtype=bool))
sns.heatmap(corr, mask=mask, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)
plt.title('Feature Correlation Heatmap')
save_plot('03-correlation-heatmap')

X = df.drop('MedHouseVal', axis=1)
y = df['MedHouseVal']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

gbr = GradientBoostingRegressor(n_estimators=100, random_state=42)
gbr.fit(X_train, y_train)
y_pred = gbr.predict(X_test)

plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.3, color='purple')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=2)
plt.title('Actual vs Predicted House Values (Gradient Boosting)')
plt.xlabel('Actual Value')
plt.ylabel('Predicted Value')
save_plot('04-model-predictions')

print("Task 6 plots generated.")
