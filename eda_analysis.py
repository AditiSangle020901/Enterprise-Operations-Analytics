import pandas as pd

# Load our main Fact Table
df = pd.read_csv("fact_sales.csv")

print("🔍 ANALYZING BUSINESS PERFORMANCE...")

# KPI 1: Total Revenue
total_revenue = df['Sales'].sum()
print(f"💰 Total Revenue: ${total_revenue:,.2f}")

# KPI 2: Overall Profit Margin
avg_margin = df['Profit Margin'].mean() * 100
print(f"📈 Average Profit Margin: {avg_margin:.2f}%")

# KPI 3: Efficiency (Shipping Time)
avg_shipping = df['Shipping Time'].mean()
print(f"🚚 Avg Shipping Delay: {avg_shipping:.2f} days")

# TREND ANALYSIS: Which Products are the 'Problem Children'?
# We'll look for products with negative profit
low_profit = df.groupby('Product ID')['Profit'].sum().sort_values().head(5)
print("\n🚩 Top 5 Loss-Making Product IDs:")
print(low_profit)

print("\nAnalysis Complete! You now have the 'Insights' for your GitHub README.")