# from flask import Flask, render_template, request, jsonify
# app = Flask(__name__)

# sales_data = {
#     'total_sales': 0,
#     'monthly_target': 5000,
#     'cumulative_sales': 0
# }

# @app.route('/')
# def index():
#     return render_template('index.html', sales_data=sales_data)

# @app.route('/add_sale', methods=['POST'])
# def add_sale():
#     product_price = float(request.form['productPrice'])
#     product_quantity = int(request.form['productQuantity'])
#     sale_amount = product_price * product_quantity

#     sales_data['total_sales'] += sale_amount
#     sales_data['cumulative_sales'] = sales_data['total_sales']

#     return jsonify(sales_data)

# if __name__ == '__main__':
#     app.run(debug=True)



# from flask import Flask, render_template, request, jsonify
# app = Flask(__name__)

# sales_data = {
#     'total_sales': 0,
#     'monthly_target': 5000,
#     'cumulative_sales': 0
# }

# @app.route('/')
# def index():
#     customers = ["Customer A", "Customer B", "Customer C"]
#     products = [
#         {"name": "Product 1", "price": 10.00},
#         {"name": "Product 2", "price": 20.00},
#         {"name": "Product 3", "price": 30.00}
#     ]
#     return render_template('index.html', sales_data=sales_data, customers=customers, products=products)

# @app.route('/add_sale', methods=['POST'])
# def add_sale():
#     try:
#         product_price = float(request.form['productPrice'])
#         product_quantity = int(request.form['productQuantity'])
#         sale_amount = product_price * product_quantity

#         sales_data['total_sales'] += sale_amount
#         sales_data['cumulative_sales'] = sales_data['total_sales']

#         return jsonify(sales_data)
#     except KeyError as e:
#         return f"Missing form field: {e}"

# if __name__ == '__main__':
#     app.run(debug=True)





from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

sales_data = {
    'total_sales': 0,
    'monthly_target': 5000,
    'cumulative_sales': 0
}

@app.route('/')
def index():
    customers = ["Customer A", "Customer B", "Customer C"]
    products = [
        {"name": "Product 1", "price": 10.00},
        {"name": "Product 2", "price": 20.00},
        {"name": "Product 3", "price": 30.00}
    ]
    return render_template('index.html', sales_data=sales_data, customers=customers, products=products)

@app.route('/add_sale', methods=['POST'])
def add_sale():
    try:
        product_price = float(request.form['productPrice'])
        product_quantity = int(request.form['productQuantity'])
        sale_amount = product_price * product_quantity

        sales_data['total_sales'] = sale_amount
        sales_data['cumulative_sales'] += sale_amount

        return jsonify(sales_data)
    except KeyError as e:
        return f"Missing form field: {e}"

if __name__ == '__main__':
    app.run(debug=True)
