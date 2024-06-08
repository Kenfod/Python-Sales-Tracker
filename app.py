from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import pytz

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sales.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'
    

# Define your local time zone
local_tz = pytz.timezone('Africa/Nairobi')  # Replace 'Your/LocalTimezone' with your actual timezone, e.g., 'America/New_York'


def get_local_time():
    utc_now = datetime.utcnow().replace(tzinfo=pytz.utc)
    local_now = utc_now.astimezone(local_tz)
    return local_now.strftime('%d-%m-%Y %H:%M:%S')

# def get_local_time():
#     return datetime.now(local_tz)

class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), nullable=False)
    customer_name = db.Column(db.String(80), nullable=False)
    product_name = db.Column(db.String(80), nullable=False)
    product_price = db.Column(db.Float, nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    total_sale = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=get_local_time)  # Use local time
    # date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Sale {self.id}>'

# Ensure the database tables are created within the application context
with app.app_context():
    db.create_all()

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def index():
    sales = Sale.query.all()
    cumulative_sales = sum(sale.total_sale for sale in sales)
    monthly_target = 200000
    customers = ['Customer A', 'Customer B', 'Customer C']
    products = [
        {'name': 'Product 1', 'price': 100},
        {'name': 'Product 2', 'price': 200},
        {'name': 'Product 3', 'price': 300}
    ]
    # return render_template('index.html', sales=sales, cumulative_sales=cumulative_sales, monthly_target=monthly_target, customers=customers, products=products, datetime=datetime)

    current_local_time = get_local_time()

    target_balance = monthly_target - cumulative_sales
    return render_template('index.html', 
                           sales=sales, 
                           cumulative_sales=cumulative_sales, 
                           monthly_target=monthly_target, 
                           customers=customers, 
                           products=products, 
                           target_balance=target_balance,
                           current_local_time=current_local_time)

                        #    datetime=datetime)

@app.route('/add', methods=['POST'])
@login_required
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
@login_required
def edit_sale(id):
    sale = Sale.query.get_or_404(id)
    customers = ['Customer A', 'Customer B', 'Customer C']
    products = [
        {'name': 'Product 1', 'price': 100},
        {'name': 'Product 2', 'price': 200},
        {'name': 'Product 3', 'price': 300}
    ]
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
@login_required
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
