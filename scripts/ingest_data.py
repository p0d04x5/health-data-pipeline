import pandas as pd
import sqlite3
import os

# ✅ Step 1: Set the correct path to your CSV file
csv_path = "data/health_data_large.csv"  # Make sure this matches your filename

# ✅ Step 2: Read the CSV into a DataFrame
df = pd.read_csv(csv_path)

# ✅ Step 3: Create/connect to SQLite database
db_path = "health.db"
conn = sqlite3.connect(db_path)

# ✅ Step 4: Write data into a table called 'health_data'
df.to_sql("health_data", conn, if_exists="replace", index=False)

# ✅ Step 5: Close the connection
conn.close()

# ✅ Step 6: Confirm success
print("✅ Data loaded into SQLite DB successfully!")
