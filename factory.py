from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri' 
db = SQLAlchemy(app) 


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ... other order-related fields (customer_id, date, status) ...

    def to_dict(self):
        return {
            'id': self.id,
            # ... include other relevant fields ...
        }

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # ... other product-related fields 

    def to_dict(self):
        return {
            'id': self.id,
            # ... include other relevant fields 
        }

@app.route('/orders')
def get_orders():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    orders = Order.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'orders': [order.to_dict() for order in orders.items],
        'total_pages': orders.pages,
        'current_page': page
    })

@app.route('/products')
def get_products():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)

    products = Product.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        'products': [product.to_dict() for product in products.items],
        'total_pages': products.pages,
        'current_page': page
    })