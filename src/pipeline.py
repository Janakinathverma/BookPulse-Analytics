import pandas as pd
import sqlite3
from datetime import datetime

DB_NAME = "data_history.db"

def clean_data(raw_data_list):
    print("[ETL] Cleaning and Transforming data...")
    df = pd.DataFrame(raw_data_list)
    
    if df.empty:
        return df

    # Data Cleaning Logic: Remove currency symbols and commas, convert to numeric
    for col in ['current_price', 'original_price']:
        df[col] = df[col].astype(str).str.replace('₹', '').str.replace(',', '').str.strip()
        df[col] = pd.to_numeric(df[col], errors='coerce')
        
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')
    
    # Feature Engineering: Calculate Discount Percentage
    df['discount_pct'] = ((df['original_price'] - df['current_price']) / df['original_price'] * 100).round(2)
    df['timestamp'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return df

def log_to_database(df):
    if df.empty:
        return
    print(f"[ETL] Logging search results to SQLite database ({DB_NAME})...")
    conn = sqlite3.connect(DB_NAME)
    # Append mode to preserve historical data entries
    df.to_sql("price_history", conn, if_exists="append", index=False)
    conn.close()