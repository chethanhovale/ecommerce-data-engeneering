print("🔥 Script started")

import pandas as pd
from sqlalchemy import create_engine

# CSV file
csv_file = "ecommerce_orders.csv"

# Load CSV
df = pd.read_csv(csv_file)
print("CSV loaded:", len(df), "rows")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:260012345@localhost:5432/postgres"
)

# Write to Postgres
df.to_sql(
    "ecommerce_orders_raw",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Table ecommerce_orders_raw created successfully")
