import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(product_id=None):
    with open('products.json', 'r') as f:
        products = json.load(f)
    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
    return products


def read_csv(product_id=None):
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price'])
            })
    if product_id is not None:
        products = [p for p in products if p['id'] == product_id]
    return products


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)

    if source == 'json':
        data = read_json(product_id)
    elif source == 'csv':
        data = read_csv(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None and not data:
        return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)