"""
Module: input_output
Responsible for parsing input commands and formatting output.
"""

class InputHandler:
    def __init__(self, input_file_path: str):
        self.input_file_path = input_file_path

    def read_commands(self):
        """
        Reads the input file line by line and yields each command as a stripped string.
        """
        with open(self.input_file_path, 'r') as file:
            for line in file:
                stripped_line = line.strip()
                if stripped_line:
                    yield stripped_line

class OutputHandler:
    def print_bill(self, bill_data):
        """
        Formats and prints the bill based on the processed data.

        Parameters:
            bill_data (dict): A dictionary containing the billing details. Expected keys:
                - sub_total: float
                - coupon_discount: tuple (coupon_name: str, discount_amount: float) or None
                - total_pro_discount: float
                - pro_membership_fee: float
                - enrollment_fee: float
                - total: float
        """
        print(f"SUB_TOTAL {bill_data.get('sub_total', 0):.2f}")

        coupon = bill_data.get('coupon_discount')
        if coupon and coupon[0]:
            print(f"COUPON_DISCOUNT {coupon[0]} {coupon[1]:.2f}")
        else:
            print("DISCOUNT NONE 0")

        print(f"TOTAL_PRO_DISCOUNT {bill_data.get('total_pro_discount', 0):.2f}")
        print(f"PRO_MEMBERSHIP_FEE {bill_data.get('pro_membership_fee', 0):.2f}")
        print(f"ENROLLMENT_FEE {bill_data.get('enrollment_fee', 0):.2f}")
        print(f"TOTAL {bill_data.get('total', 0):.2f}")
