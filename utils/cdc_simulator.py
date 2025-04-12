# utils/cdc_simulator.py
import random
from utils.db import insert_dummy_sale

def simulate_cdc():
    customers = ["Alexander", "Sabrina", "John", "Maria"]
    products = ["Solar Panel", "Battery", "Inverter", "EV Charger"]
    customer = random.choice(customers)
    product = random.choice(products)
    quantity = random.randint(1, 5)

    price_map = {
        "Solar Panel": 500,
        "Battery": 600,
        "Inverter": 700,
        "EV Charger": 800
    }

    amount = quantity * price_map[product]
    insert_dummy_sale(customer, product, quantity, amount)
