import csv
import random
from datetime import datetime, timedelta

# Helper functions
def random_date(start, end):
    return start + timedelta(
        seconds=random.randint(0, int((end - start).total_seconds())),
    )

def generate_fake_transaction():
    types = ['purchase', 'refund', 'transfer', 'withdrawal', 'deposit']
    products = ['Book', 'Electronics', 'Clothing', 'Groceries', 'Furniture']
    descriptions = [
        'Bought a book', 'Refund for electronics', 'Transferred funds', 
        'Withdrew cash', 'Deposited salary'
    ]
    currencies = ['USD', 'EUR', 'GBP', 'JPY', 'AUD']
    states = ['completed', 'pending', 'failed', 'cancelled']

    start_date = random_date(datetime(2024, 6, 1), datetime(2024, 6, 25))
    completed_date = start_date + timedelta(days=random.randint(1, 30))

    transaction = {
        'Type': random.choice(types),
        'Product': random.choice(products),
        'Started Date': start_date.strftime('%Y-%m-%d %H:%M:%S'),
        'Completed Date': completed_date.strftime('%Y-%m-%d %H:%M:%S'),
        'Description': random.choice(descriptions),
        'Amount': round(random.uniform(10, 500), 2),
        'Fee': round(random.uniform(1, 20), 2),
        'Currency': random.choice(currencies),
        'State': random.choice(states),
        'Balance': round(random.uniform(500, 10000), 2),
    }

    return transaction

# Generate 20 fake transactions
transactions = [generate_fake_transaction() for _ in range(20)]

# Write to CSV file
csv_file_path = r'C:\Users\DON\Desktop\csv-generator\solution.csv'
fieldnames = [
    'Type', 'Product', 'Started Date', 'Completed Date', 'Description', 
    'Amount', 'Fee', 'Currency', 'State', 'Balance'
]

with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(transactions)

csv_file_path
