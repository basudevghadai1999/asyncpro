from flask import Flask, request, jsonify
import asyncio

app = Flask(__name__)

# In-memory product database (initially empty)
products = {
    1: {"name": "Product A", "quantity": 10, "price": 29.99},
    2: {"name": "Product B", "quantity": 200, "price": 19.99},
    3: {"name": "Product C", "quantity": 50, "price": 49.99},
    4: {"name": "Product D", "quantity": 150, "price": 9.99}
}

# Asynchronous function to simulate updating inventory
async def update_inventory_async(product_id, quantity):
    await asyncio.sleep(1)  # Simulate async task (e.g., waiting for a DB update)
    if product_id in products:
        products[product_id]['quantity'] += quantity

# Route for adding a new product (synchronous)
@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.get_json()  # Get data from the request body
    product_id = data['id']
    name = data['name']
    quantity = data['quantity']
    price = data['price']

    # Add new product or update existing one
    products[product_id] = {'name': name, 'quantity': quantity, 'price': price}

    print(products)

    return jsonify({"message": "Product added"})

# Route for updating product stock asynchronously
@app.route('/update_stock', methods=['POST'])
async def update_stock():
    data = request.get_json()  # Get data from the request body
    product_id = data['id']
    quantity = data['quantity']

    # Simulate asynchronous inventory update
    await update_inventory_async(product_id, quantity)

    # Return response after async task completes
    return jsonify({"message": "Stock updated asynchronously"})

# Route for logging a sale (reduce stock)
@app.route('/log_sale', methods=['POST'])
async def log_sale():
    data = request.get_json()  # Get data from the request body
    product_id = data['id']
    quantity_sold = data['quantity']

    # Check if product exists and if enough stock is available
    if product_id in products and products[product_id]['quantity'] >= quantity_sold:
        # Simulate async task (e.g., logging the sale in the DB)
        await asyncio.sleep(1)  # Simulate async task duration
        products[product_id]['quantity'] -= quantity_sold
        return jsonify({"message": "Sale logged"})

    # If there's insufficient stock
    return jsonify({"message": "Insufficient stock"}), 400

if __name__ == '__main__':
    app.run(debug=True)
