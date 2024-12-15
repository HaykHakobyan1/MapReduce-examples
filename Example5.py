from collections import defaultdict

# Sample input: Each line contains product_id, quantity, price
input_data = [
    "101, 2, 50.0",  # Product 101, Quantity 2, Price 50.0
    "102, 1, 30.0",  # Product 102, Quantity 1, Price 30.0
    "101, 1, 50.0",  # Product 101, Quantity 1, Price 50.0
    "103, 4, 20.0",  # Product 103, Quantity 4, Price 20.0
    "102, 2, 30.0"   # Product 102, Quantity 2, Price 30.0
]

def mapper(input_data):
    """Map step: Emit (product_id, quantity * price) for each line."""
    mapped_data = []
    for line in input_data:
        product_id, quantity, price = line.split(",")  # Split into fields
        product_id = product_id.strip()
        quantity = int(quantity.strip())
        price = float(price.strip())
        total_sale = quantity * price  # Calculate total sale for the line
        mapped_data.append((product_id, total_sale))  # Emit (product_id, total_sale)
    return mapped_data

def reducer(mapped_data):
    """Reduce step: Sum the total sales for each product."""
    product_sales = defaultdict(float)
    for product_id, total_sale in mapped_data:
        product_sales[product_id] += total_sale  # Aggregate sales for each product
    return product_sales

# Map Step
mapped_data = mapper(input_data)

# Reduce Step
product_sales = reducer(mapped_data)

# Output Results
print("Total Sales for Each Product:")
for product_id, total_sale in product_sales.items():
    print(f"Product {product_id}: ${total_sale:.2f}")