from flask import Flask,request,jsonify

import asyncio

app = Flask(__name__)


#created a empty dictionary
products = {}



products = {
    1: {"name": "Product A", "quantity": 10, "price": 29.99},
    2: {"name": "Product B", "quantity": 200, "price": 19.99},
    3: {"name": "Product C", "quantity": 50, "price": 49.99},
    4: {"name": "Product D", "quantity": 150, "price": 9.99}
}



#Asynchronous function to simulate updating inventory

async def update_inventory_async(product_id,quanity):
    await asyncio.sleep(1) # Simulate async task
    if product_id in products:
        products[product_id]['quantity'] += quanity


# for adding a product
@app.route('/add_product',methods=['POST'])
def add_product():
    
    data = request.get_json() # getting data 
    product_id = data['id']
    name = data['name']
    quantity = data['quantity']
    price = data['price']
    products[product_id] = {'name':name,'quantity':quantity,'price':price}

    print(products)

    return jsonify({"message":"Product added"})


#for updating the stock
@app.route('/update_stock',methods=['POST'])
def update_stock():
    data = request.get_json()

    product_id = data['id']
    quantity = data['quantity']

    # if product_id in products:
    #     products[product_id]['quanity'] += quanity

    #     return jsonify({"message":"Stock updated"})
    return jsonify({"message":"product not found"}),404




@app.route('/log_sale',methods=['POST'])
def log_sale():
    data = request.get_json()
    product_id = data['id']
    quanity_sold = data['quantity']



    if product_id in products and products[product_id]['quantity'] >= quanity_sold:
        await asyncio.sleep(1)
        products[product_id]['quantity'] -= quanity_sold
        return jsonify({"message":"Sale logged"})

    return jsonify({"message":"Insufficient stock"}),400

if __name__ == '__main__':
    app.run(debug=True)

