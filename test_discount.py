from discount import calculate_discount
def test_vip_customer():
    assert calculate_discount(60000000, 20000000) == 0.1

def test_premium_customer():
    assert calculate_discount(490000000, 20000000) == 0.1
def test_vip_customer_edge_case():
    assert calculate_discount(50000000, 20000000) == 0.1