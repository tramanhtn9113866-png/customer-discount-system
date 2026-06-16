def calculate_discount(total_before_order, order_amount_new):
    if total_before_order >= 50000000:
        return 0.1
    if total_before_order + order_amount_new >= 50000000:
        return 0.1
    return 0