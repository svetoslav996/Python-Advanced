import json
import os

from global_constants import *


def get_all_products():
    products = []
    with open(os.path.join(DB_FOLDER_NAME, PRODUCTS_IMAGES_FOLDER_NAME), 'r') as file:
        for line in file:
            products.append(json.loads(line.strip()))
        print(products)
        return products
