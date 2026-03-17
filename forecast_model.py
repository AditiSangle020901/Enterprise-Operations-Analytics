import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# 1. Load data
df = pd.read_csv("fact_sales.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])

# 2. Prepare data: Total Sales per Month
df['Month_Year'] = df['Order Date'].dt.to_period('M')
monthly_sales = df.groupby('Month_Year')['Sales'].sum().reset_index()

# Convert time to a number (1, 2, 3...) so the math works
monthly_sales['Month_Count'] = np.arange(len(monthly_sales))

# 3. Build the Model
X = monthly_sales[['Month_Count']] # Input: The month number
y = monthly_sales['Sales']       # Output: The sales $

model = LinearRegression()
model.fit(X, y)

# 4. Predict next month (the next number in the sequence)
next_month = np.array([[len(monthly_sales)]])
prediction = model.predict(next_month)

print(f"🔮 FORECAST: Predicted Sales for next month: ${prediction[0]:,.2f}")