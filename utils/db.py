# utils/db.py
from sqlalchemy import create_engine, text
import pandas as pd

# Koneksi ke dummy SQLite (simulasi PostgreSQL CDC / Snowflake)
engine = create_engine("sqlite:///data/dummy_source.sqlite", echo=False)

def get_latest_sales(limit=100):
    query = text("""
        SELECT * FROM sales
        ORDER BY created_at DESC
        LIMIT :limit
    """)
    with engine.connect() as conn:
        return pd.read_sql(query, conn, params={"limit": limit})

def insert_dummy_sale(customer, product, quantity, amount):
    query = text("""
        INSERT INTO sales (customer, product, quantity, amount)
        VALUES (:customer, :product, :quantity, :amount)
    """)
    with engine.connect() as conn:
        conn.execute(query, {
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "amount": amount
        })
        conn.commit()
