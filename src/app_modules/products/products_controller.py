from src.app_modules.products import products_service


def get_products():
    return products_service.get_products()
