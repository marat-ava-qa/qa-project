from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    URL = "https://www.saucedemo.com"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def get_error(self):
        error = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']"))
        )
        return error.text
    
    def is_login_button_visible(self):
        button = self.wait.until(
        EC.visibility_of_element_located((By.ID, "login-button"))
    )
        return button is not None

class ProductsPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_title(self):
        title = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "title"))
        )
        return title.text
    
    def add_backpack_to_cart(self):
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()


    def get_cart_badge_count(self):
        badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )
        return badge.text
    
    
class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def get_first_item_name(self):
        first = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_item_name"))
            )
        return  first.text
    
