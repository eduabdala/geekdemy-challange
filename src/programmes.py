"""
Module: programmes

This module defines available education programmes and their associated costs.
It provides the `Programme` class to calculate the total cost based on 
programme category and quantity.
"""

# Dictionary mapping programme categories to their unit prices
PROGRAM_PRICES = {
    'CERTIFICATION': 3000,
    'DEGREE': 5000,
    'DIPLOMA': 2500,
}

class Programme:
    """
    Represents an education programme with a specific category and quantity.

    Attributes:
        category (str): The type of programme (e.g., 'CERTIFICATION', 'DEGREE', 'DIPLOMA').
        quantity (int): The number of programme units enrolled.
        unit_price (float): The price of a single programme unit.

    Methods:
        total_price(): Calculates and returns the total cost.
    """

    def __init__(self, category: str, quantity: int):
        """
        Initialize a Programme instance.

        Args:
            category (str): The programme category.
            quantity (int): The quantity of the programme to enroll in.
        """
        self.category = category.upper()
        self.quantity = quantity
        self.unit_price = PROGRAM_PRICES.get(self.category, 0)

    def total_price(self) -> float:
        """
        Calculate the total price for the programme.

        Returns:
            float: The total cost (unit_price * quantity).
        """
        return self.unit_price * self.quantity
