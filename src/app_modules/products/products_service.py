from src.app_modules.products import products_dao

def get_products():
    return products_dao.get_products()
