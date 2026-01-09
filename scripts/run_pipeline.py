import pandas as pd
import os
from sqlalchemy import create_engine, text

print("🚀 Pipeline started")

# ---------- DATABASE CONFIG ----------
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")


engine = create_engine(
    f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# ---------- LOAD CSV ----------
csv_path = "C:/Users/chethan hovale/Desktop/ecommerce-data-engeneering/data/ecommerce_orders.csv"
df = pd.read_csv(csv_path)

print(f"📄 CSV loaded: {len(df)} rows")

# ---------- RAW LAYER ----------
df.to_sql(
    "ecommerce_orders_raw",
    engine,
    schema="raw",
    if_exists="replace",
    index=False
)
print("✅ RAW layer loaded")

# ---------- CLEAN LAYER ----------
with engine.begin() as conn:
    conn.execute(text("""
        DROP TABLE IF EXISTS clean.ecommerce_orders_clean;

        CREATE TABLE clean.ecommerce_orders_clean AS
        SELECT
            order_id,
            order_date::date,
            customer_id,
            customer_name,
            city,
            payment_method,
            quantity,
            price,
            order_status
        FROM raw.ecommerce_orders_raw
        WHERE order_status = 'Delivered'
          AND quantity > 0
          AND price > 0;
    """))

print("✅ CLEAN layer created")

# ---------- ANALYTICS LAYER ----------
with engine.begin() as conn:
    conn.execute(text("""
        DROP TABLE IF EXISTS analytics.fact_orders CASCADE;

        CREATE TABLE analytics.fact_orders AS
        SELECT
            order_id,
            order_date,
            customer_id,
            city,
            payment_method,
            quantity,
            price,
            quantity * price AS order_amount
        FROM clean.ecommerce_orders_clean;
    """))

print("✅ ANALYTICS layer created")
print("🎉 Pipeline completed successfully")
