from sys import argv
from src.input_output import InputHandler, OutputHandler
from src.programmes import Programme
from src.membership import Membership
from src.coupons import B4G1Coupon, DealG20Coupon, DealG5Coupon
from src.cart import Cart
from src.billing import Billing

def main():
    if len(argv) != 2:
        raise Exception("File path not entered. Usage: python main.py <input_file_path>")

    input_file = argv[1]

    input_handler = InputHandler(input_file)
    output_handler = OutputHandler()
    cart = Cart()
    membership = Membership(is_pro_member=False)
    applied_coupons = []

    # Mapeamento dos nomes de cupom para as classes
    coupon_classes = {
        "B4G1": B4G1Coupon,
        "DEAL_G20": DealG20Coupon,
        "DEAL_G5": DealG5Coupon,
    }

    for command_line in input_handler.read_commands():
        # Exemplo de comando: ADD_PROGRAMME CERTIFICATION 1
        parts = command_line.split()
        if not parts:
            continue
        cmd = parts[0]

        if cmd == "ADD_PROGRAMME" and len(parts) == 3:
            category = parts[1]
            quantity = int(parts[2])
            programme = Programme(category, quantity)
            cart.add_product(programme)

        elif cmd == "ADD_PRO_MEMBERSHIP":
            membership.is_pro_member = True

        elif cmd == "APPLY_COUPON" and len(parts) == 2:
            coupon_name = parts[1]
            if coupon_name in coupon_classes:
                coupon_instance = coupon_classes[coupon_name](coupon_name)
                applied_coupons.append(coupon_instance)

        elif cmd == "PRINT_BILL":
            # Checar as regras e criar a fatura
            billing = Billing(cart.items, membership, applied_coupons)

            sub_total = billing.calculate_subtotal()
            coupon_discount = billing.apply_coupons()
            total_pro_discount = membership.calculate_total_pro_discount(cart.items)
            pro_membership_fee = membership.get_membership_fee()
            enrollment_fee = billing.calculate_enrollment_fee(sub_total - coupon_discount)
            total = sub_total - coupon_discount - total_pro_discount + pro_membership_fee + enrollment_fee

            bill_data = {
                'sub_total': sub_total,
                'coupon_discount': ("COUPON", coupon_discount),
                'total_pro_discount': total_pro_discount,
                'pro_membership_fee': pro_membership_fee,
                'enrollment_fee': enrollment_fee,
                'total': total
            }
            output_handler.print_bill(bill_data)

if __name__ == "__main__":
    main()
