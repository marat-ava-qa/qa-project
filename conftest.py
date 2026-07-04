import pytest
@pytest.fixture
def product():
    return{
        "name": "iPhone",
        "price": 80000,
        "in_stock": True
    }
    
