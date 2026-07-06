def test_product_name(product):
    assert product["name"] == "iPhone"

def test_product_price(product):
    assert product["price"] == 80000

def test_product_in_stock(product):
    assert product["in_stock"] 