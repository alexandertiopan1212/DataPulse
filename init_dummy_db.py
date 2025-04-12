# init_dummy_db.py
import sqlite3
import os

# Buat folder /data kalau belum ada
os.makedirs("data", exist_ok=True)

conn = sqlite3.connect("data/dummy_source.sqlite")
cursor = conn.cursor()

# Buat tabel dummy
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    product TEXT,
    quantity INTEGER,
    amount REAL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Isi data awal
sample_data = [
    ("Alice", "Solar Panel", 3, 1500.0),
    ("Bob", "Inverter", 1, 700.0),
    ("Charlie", "Battery", 2, 1200.0),
]

cursor.executemany("INSERT INTO sales (customer, product, quantity, amount) VALUES (?, ?, ?, ?)", sample_data)
conn.commit()
conn.close()

print("✅ dummy_source.sqlite berhasil dibuat di folder /data")
