from flask import Blueprint, request, jsonify

from models import Product, db

product_blueprint = Blueprint('product_api_routes', __name__, url_prefix='/api/product')


@product_blueprint.route('/all', methods=['GET'])
def get_all_products():
    all_products = Product.query.all()
    result = [product.serialize() for product in all_products]
    response = {"result":result}
    return jsonify(response)


@product_blueprint.route('/create', methods=['POST'])
def create_products():
    try:
        product = Product()
        product.name = request.form['name']
        product.slug = request.form['slug']
        product.image = request.form['image']
        product.price = request.form['price']

        db.session.add(product)
        db.session.commit()

        response = {'message': 'Product Created', 'result': product.serialize()}
    except Exception as e:
        print(str(e))
        response = {'message': 'Product creation failed'}

    return jsonify(response)


@product_blueprint.route('/<slug>', methods=['GET'])
def product_details(slug):
    product = Product.query.filter_by(slug=slug).first()
    if product:
        response = {"result":product.serialize()}
    else:
        response = {"message":"No products found"}

    return jsonify(response)
