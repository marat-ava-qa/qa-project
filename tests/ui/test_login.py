from selenium import webdriver
import pytest 
from pages.login_page import LoginPage, ProductsPage, CartPage
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()                     
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    yield driver 
    driver.quit()
    
    
def test_successful_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductsPage(driver)
    assert products_page.get_title() == "Products"
    
    
def test_wrong_password(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    
    assert "do not match" in login_page.get_error()
    
    
def test_login_button_visible(driver):
    login_page = LoginPage(driver)
    login_page.open()
    
    assert login_page.is_login_button_visible()
    
def test_add_to_cart(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    
    products_page = ProductsPage(driver)
    products_page.add_backpack_to_cart()
    assert products_page.get_cart_badge_count() == "1"
    
    cart_page = CartPage(driver)
    cart_page.open_cart()
    assert cart_page.get_first_item_name() == "Sauce Labs Backpack"