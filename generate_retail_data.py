import typing_extensions
from numpy import random
import pandas as pd
import numpy as np  
from datetime import datetime, timedelta

print("--- [INITIALIZING SIMULATION ENGINE] ---")

np.random.seed(42)

num_customers = 1000
num_transactions = 5000

customers_ids = [f"CUST_{i:04d}" for i in range(1, num_customers + 1)]
start_date = datetime(2025,1,1)

tx_records = []

print(f"Simulating {num_transactions} e-commerce records spanning across 1 year...")

for _ in range(num_transactions):
    cust = np.random.choice(customers_ids)

    days_to_add = np.random.randint(0,365)
    tx_date = start_date + timedelta(days= days_to_add)

    order_value = np.round(np.random.exponential(scale=45.0) + 7.5,2)
    
    tx_records.append({
        'InvoiceID': f"INV_{np.random.randint(100000,999999)}",
        'CustomerID': cust,
        'InvoiceDate': tx_date.strftime('%Y-%m-%d'),
        'PurchaseAmount': order_value,
        
    })

df = pd.DataFrame(tx_records)

df.loc[df.sample(frac=0.03).index, 'CustomerID']= np.nan

df.to_csv('raw_data/retail_transactions.csv', index=False)

print("[SUCCESS] 'retail_transactions.csv' generated with exactly 5,000 rows.")