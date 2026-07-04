import pytest

@pytest.fixture
def product():
    return{
        "name": "iPhone",
        "price": 80000,
        "in_stock": True
    }
    
def test_product_name(product):
    assert product["name"] == "iPhone"

def test_product_price(product):
    assert product["price"] == 80000

def test_product_in_stock(product):
    assert product["in_stock"] 