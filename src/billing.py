"""
Module: billing
Handles calculation of subtotals, discounts, fees, and totals.
"""

from typing import List
from .programmes import Programme
from .membership import Membership
from .coupons import Coupon


class Billing:
    def __init__(self, programmes: List[Programme], membership: Membership, coupons: List[Coupon]):
        """
        Initializes the Billing instance.

        :param programmes: List of Programme instances purchased
        :param membership: ProMembership instance (if user has membership)
        :param coupons: List of applied Coupon instances
        """
        self.programmes = programmes
        self.membership = membership
        self.coupons = coupons

    def calculate_subtotal(self) -> float:
        """
        Calculates the subtotal after applying membership discounts to each programme.

        :return: Discounted subtotal price
        """
        subtotal = 0.0
        for programme in self.programmes:
            discount = 0.0
            if self.membership.is_pro_member:
                discount = self.membership.get_discount_for_programme(programme.category, programme.unit_price)
            discounted_price_per_unit = programme.unit_price - discount
            subtotal += discounted_price_per_unit * programme.quantity
        return subtotal

    def apply_coupons(self) -> float:
        """
        Applies coupons to the subtotal and returns the total discount value from coupons.

        :return: Total coupon discount amount
        """
        subtotal = self.calculate_subtotal()
        max_discount = 0.0

        for coupon in self.coupons:
            discount = coupon.calculate_discount(subtotal, self.programmes)
            if discount > max_discount:
                max_discount = discount

        return max_discount

    def calculate_enrollment_fee(self, subtotal: float) -> float:
        """
        Calculates enrollment fee based on subtotal.
        If subtotal < 6666, fee is Rs. 500, otherwise it's Rs. 0.

        :param subtotal: Subtotal after discounts
        :return: Enrollment fee amount
        """
        return 500.0 if subtotal < 6666 else 0.0

    def calculate_total(self) -> float:
        """
        Calculates the final total amount after applying membership discounts,
        coupon discounts, and enrollment fee.

        :return: Final total payable amount
        """
        subtotal = self.calculate_subtotal()
        coupon_discount = self.apply_coupons()
        subtotal_after_coupon = subtotal - coupon_discount
        enrollment_fee = self.calculate_enrollment_fee(subtotal_after_coupon)
        pro_membership_fee = self.membership.get_membership_fee()
        total = subtotal_after_coupon + enrollment_fee + pro_membership_fee
        return total