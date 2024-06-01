from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    customer_name = db.Column(db.String(80), nullable=False)
    product_name = db.Column(db.String(80), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    total_sale = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Sale {self.id}>'

# Enclose the database initialization in an application context
with app.app_context():
    db.create_all()

# Example data for customers and products
customers = ['Customer A', 'Customer B', 'Customer C']
products = [
    {'name': 'Product 1', 'price': 10.00},
    {'name': 'Product 2', 'price': 20.00},
    {'name': 'Product 3', 'price': 30.00},
]

@app.route('/')
def index():
    sales = Sale.query.all()
    cumulative_sales = sum(sale.total_sale for sale in sales)
    monthly_target = 5000.0
    return render_template('index.html', sales=sales, cumulative_sales=cumulative_sales, monthly_target=monthly_target, customers=customers, products=products)

@app.route('/add', methods=['POST'])
def add_sale():
    user_name = request.form['userName']
    customer_name = request.form['customerName']
    product_name = request.form['productName']
    product_price = float(request.form['productPrice'])
    product_quantity = int(request.form['productQuantity'])
    total_sale = product_price * product_quantity

    new_sale = Sale(
        user_name=user_name,
        customer_name=customer_name,
        product_name=product_name,
        product_price=product_price,
        product_quantity=product_quantity,
        total_sale=total_sale
    )

    try:
        db.session.add(new_sale)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"An error occurred while adding the sale: {e}"

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_sale(id):
    sale = Sale.query.get_or_404(id)
    if request.method == 'POST':
        sale.user_name = request.form['userName']
        sale.customer_name = request.form['customerName']
        sale.product_name = request.form['productName']
        sale.product_price = float(request.form['productPrice'])
        sale.product_quantity = int(request.form['productQuantity'])
        sale.total_sale = sale.product_price * sale.product_quantity

        try:
            db.session.commit()
            return redirect('/')
        except Exception as e:
            return f"An error occurred while updating the sale: {e}"
    else:
        return render_template('edit.html', sale=sale, customers=customers, products=products)

@app.route('/delete/<int:id>')
def delete_sale(id):
    sale = Sale.query.get_or_404(id)
    try:
        db.session.delete(sale)
        db.session.commit()
        return redirect('/')
    except Exception as e:
        return f"An error occurred while deleting the sale: {e}"

if __name__ == '__main__':
    app.run(debug=True)
