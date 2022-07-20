from app import app
from flask import render_template
from models.order import orders

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orders')
def get_all_orders():
    return render_template('orders.html', orders=orders)

@app.route('/orders/<id>')
def get_order_by_id(id):
    return render_template('order.html', order=orders[int(id)])
    