"""
Module: cart
Handles adding and storing selected products/programmes.
"""

class Cart:
    def __init__(self):
        """
        Initialize an empty cart.
        """
        self.items = []  # List of Product instances

    def add_product(self, product):
        """
        Add a product to the cart.

        :param product: A Product instance
        """
        self.items.append(product)

    def get_items(self):
        """
        Get all products in the cart.

        :return: List of Product instances
        """
        return self.items

    def __repr__(self):
        return f"Cart({self.items})"
