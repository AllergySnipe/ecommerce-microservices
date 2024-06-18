import requests

from . import PRODUCT_API_URL


class ProductClient:
    @staticmethod
    def get_products():
        response = requests.get(PRODUCT_API_URL + '/api/product/all')
        return response.json()

    @staticmethod
    def get_product(slug):
        response = requests.get(PRODUCT_API_URL + '/api/product/' + slug)
        return response.json()
