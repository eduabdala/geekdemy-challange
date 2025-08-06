"""
Module: product
Defines the Product class used to represent individual items available for enrollment.
"""

class Product:
    def __init__(self, name: str, price: float):
        """
        Initialize a new product.

        :param name: Name of the product
        :param price: Price of the product
        """
        self.name = name
        self.price = price

    def __repr__(self):
        return f"Product(name={self.name}, price={self.price})"
