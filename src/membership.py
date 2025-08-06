"""
Module: membership
Handles Pro Membership logic and its related discounts.
"""

from .programmes import PROGRAM_PRICES

# Membership configuration
PRO_MEMBERSHIP_FEE = 200
PRO_MEMBERSHIP_DISCOUNTS = {
    'DIPLOMA': 0.01,        # 1% discount
    'CERTIFICATION': 0.02,  # 2% discount
    'DEGREE': 0.03          # 3% discount
}

class Membership:
    def __init__(self, is_pro_member: bool = False):
        """
        Initializes a membership object.

        Args:   
            is_pro_member (bool): Whether the user opted for Pro Membership.
        """
        self.is_pro_member = is_pro_member

    def get_membership_fee(self) -> int:
        """
        Returns the membership fee, if Pro Membership is selected.

        Returns:
            int: Rs.200 if Pro Membership, otherwise 0.
        """
        return PRO_MEMBERSHIP_FEE if self.is_pro_member else 0

    def get_discount_for_programme(self, category: str, base_price: float) -> float:
        """
        Calculates membership discount for a specific programme.

        Args:
            category (str): The programme category.
            base_price (float): The base price after any normal discount.

        Returns:
            float: Discount amount based on Pro Membership (0 if not Pro).
        """
        if not self.is_pro_member:
            return 0.0
        discount_rate = PRO_MEMBERSHIP_DISCOUNTS.get(category.upper(), 0.0)
        return base_price * discount_rate

    def calculate_total_pro_discount(self, programmes: list) -> float:
        """
        Calculates the total membership discount for a list of programmes.

        Args:
            programmes (list): List of Programme instances.

        Returns:
            float: Total discount amount from membership.
        """
        if not self.is_pro_member:
            return 0.0

        total_discount = 0.0
        for programme in programmes:
            base_price = programme.total_price()
            discount = self.get_discount_for_programme(programme.category, base_price)
            total_discount += discount

        return total_discount
