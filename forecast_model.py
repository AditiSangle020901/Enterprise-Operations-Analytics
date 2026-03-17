import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np
import warnings

# Suppress minor technical warnings for a cleaner output
warnings.filterwarnings("ignore", category=UserWarning)

# 1. Load the cleaned data
df = pd.read_csv('fact_sales.csv')
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 2. Prepare data for Time Series (Monthly Sales - using 'ME' for Month End)
df_monthly = df.set_index('Order Date').resample('ME')['Sales'].sum().reset_index()
df_monthly['Month_Index'] = np.arange(len(df_monthly))

# 3. Train the Linear Regression Model
# We use .values to avoid the "feature names" warning
X = df_monthly[['Month_Index']].values
y = df_monthly['Sales'].values
model = LinearRegression()
model.fit(X, y)

# 4. Predict for the Next Month
next_month_index = np.array([[len(df_monthly)]])
prediction = model.predict(next_month_index)[0]

# 5. Professional Visualization
plt.figure(figsize=(10, 6))
plt.plot(df_monthly['Order Date'], df_monthly['Sales'], marker='o', label='Historical Monthly Sales', color='#2c3e50')
plt.axhline(y=df_monthly['Sales'].mean(), color='gray', linestyle='--', label='Average Sales')

# Plot the Prediction point
future_date = df_monthly['Order Date'].iloc[-1] + pd.DateOffset(months=1)
plt.scatter(future_date, prediction, color='red', s=100, label=f'Predicted: ${prediction:,.2f}', zorder=5)

# Formatting
plt.title('Enterprise Sales Forecast: Historical vs. Predicted', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Total Sales ($)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

print(f"🔮 FORECAST: Predicted Sales for next month: ${prediction:,.2f}")

# This will open the graph window
plt.show()
