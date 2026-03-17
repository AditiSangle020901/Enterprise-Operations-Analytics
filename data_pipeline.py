import pandas as pd
import os

# --- 1. SETUP ---
raw_file = "Global Superstore.csv"

def run_pipeline():
    print("🚀 Starting the FINAL Enterprise Operations Pipeline...")

    if not os.path.exists(raw_file):
        print(f"❌ Error: {raw_file} not found.")
        return

    # --- 2. LOAD & BASIC CLEAN ---
    df = pd.read_csv(raw_file, encoding='latin1')
    df = df.drop_duplicates()
    df['Postal Code'] = df['Postal Code'].fillna(0)

    # --- 3. FIX DATES ---
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Ship Date'] = pd.to_datetime(df['Ship Date'])

    # --- 4. CALCULATE KPIs (Crucial!) ---
    df['Profit Margin'] = df['Profit'] / df['Sales']
    # This creates the 'Shipping Time' column Power BI is looking for
    df['Shipping Time'] = (df['Ship Date'] - df['Order Date']).dt.days

    # --- 5. STAR SCHEMA MODELING ---
    print("🛠️  Modeling Data into SQL Star Schema...")

    # dim_products
    dim_products = df[['Product ID', 'Product Name', 'Category', 'Sub-Category']].drop_duplicates(subset=['Product ID'])
    dim_products.to_csv("dim_products.csv", index=False)

    # dim_customers
    dim_customers = df[['Customer ID', 'Customer Name', 'Segment']].drop_duplicates(subset=['Customer ID'])
    dim_customers.to_csv("dim_customers.csv", index=False)

    # dim_geography
    dim_geography = df[['City', 'State', 'Country', 'Market', 'Region']].drop_duplicates()
    dim_geography.to_csv("dim_geography.csv", index=False)

    # fact_sales (WE INCLUDED EVERYTHING HERE)
    fact_sales = df[['Order ID', 'Order Date', 'Customer ID', 'Product ID', 'Country', 'Sales', 'Quantity', 'Profit', 'Shipping Cost', 'Profit Margin', 'Shipping Time']]
    fact_sales.to_csv("fact_sales.csv", index=False)

    print("✅ ALL MISSIONS COMPLETE! Everything is ready for Power BI.")

if __name__ == "__main__":
    run_pipeline()