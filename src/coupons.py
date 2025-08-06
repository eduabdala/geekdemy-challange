"""
Module: coupons
Handles all logic related to discount coupons validation and application.
"""

from typing import List
from .cart import Cart
from .product import Product

class Coupon:
    """
    Base class for all coupon types. Provides interface for validation and discount logic.
    """

    def __init__(self, name: str):
        self.name = name

    def is_applicable(self, cart: Cart) -> bool:
        """
        Check if the coupon is applicable to the current cart.

        :param cart: The cart instance.
        :return: True if applicable, False otherwise.
        """
        raise NotImplementedError("Subclasses must implement this method")

    def apply_discount(self, cart: Cart) -> float:
        """
        Apply the coupon discount to the cart.
        
        :param cart: The cart instance.
        :return: The amount of discount applied.
        """
        raise NotImplementedError("Subclasses must implement this method")


class B4G1Coupon(Coupon):
    """
    Buy 4 Get 1 Free: For every 4 items in the cart, 1 (cheapest) is free.
    """

    def is_applicable(self, cart: Cart) -> bool:
        return cart.total_quantity() >= 4

    def apply_discount(self, cart: Cart) -> float:
        if not self.is_applicable(cart):
            return 0.0

        # Sort items by price ascending and get 1 free for each 4 bought
        all_items: List[Product] = []
        for item in cart.items:
            all_items.extend([item.product] * item.quantity)

        all_items.sort(key=lambda p: p.price)
        free_items_count = cart.total_quantity() // 4

        discount = sum(item.price for item in all_items[:free_items_count])
        return discount


class DealG20Coupon(Coupon):
    """
    Apply 20% discount if cart total exceeds 10,000.
    """

    def is_applicable(self, cart: Cart) -> bool:
        return cart.total_amount() > 10000

    def apply_discount(self, cart: Cart) -> float:
        if not self.is_applicable(cart):
            return 0.0
        return 0.2 * cart.total_amount()


class DealG5Coupon(Coupon):
    """
    Apply 5% discount if all items are 'GROCERY' category.
    """

    def is_applicable(self, cart: Cart) -> bool:
        return all(item.product.category.upper() == "GROCERY" for item in cart.items)

    def apply_discount(self, cart: Cart) -> float:
        if not self.is_applicable(cart):
            return 0.0
        return 0.05 * cart.total_amount()
