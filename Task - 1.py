from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Setup browser
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

#Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

#Sort products by Price (low to high)
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_visible_text("Price (low to high)")
time.sleep(2)

#Get product details
first_product = driver.find_elements(By.CLASS_NAME, "inventory_item")[0]
product_name = first_product.find_element(By.CLASS_NAME, "inventory_item_name").text
product_price = first_product.find_element(By.CLASS_NAME, "inventory_item_price").text
first_product.find_element(By.TAG_NAME, "button").click()

#Go to Cart
driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
time.sleep(2)

#Verify name, price, quantity
cart_item = driver.find_element(By.CLASS_NAME, "cart_item")
cart_name = cart_item.find_element(By.CLASS_NAME, "inventory_item_name").text
cart_price = cart_item.find_element(By.CLASS_NAME, "inventory_item_price").text
cart_quantity = cart_item.find_element(By.CLASS_NAME, "cart_quantity").text

assert cart_name == product_name, f" Product name mismatch: {cart_name} vs {product_name}"
assert cart_price == product_price, f" Price mismatch: {cart_price} vs {product_price}"
assert cart_quantity == "1", f" Quantity mismatch: {cart_quantity} vs 1"

print("Task 1 Passed: Product added correctly with right name, price, and quantity.")


driver.quit()
