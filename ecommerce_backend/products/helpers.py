# products/helpers.py
def calculate_discounted_price(product):
    """
    Example helper to calculate final price after discount.
    """
    if product.discount_percentage:
        return product.price - (product.price * (product.discount_percentage / 100))
    return product.price
