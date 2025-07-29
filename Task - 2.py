from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

# Setup
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("error_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()
time.sleep(2)

# Sort by Name (Z to A)
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_visible_text("Name (Z to A)")
time.sleep(2)

# Extract first 3 product titles and their prices
products = driver.find_elements(By.CLASS_NAME, "inventory_item")

print("Top 3 Products after sorting by 'Name (Z to A)':")
for product in products[:3]:
    name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
    price = product.find_element(By.CLASS_NAME, "inventory_item_price").text
    print(f"- {name} - {price}")


driver.quit()
