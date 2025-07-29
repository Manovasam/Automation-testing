# Saucedemo Automation Tasks - Python + Selenium

This project automates test cases for(https://www.saucedemo.com/) using Python and Selenium WebDriver.  
It includes:

- Task 1: Add the cheapest product to the cart and verify it.
- Task 2: Sort by name and extract the top 3 product names and prices.

---

## Prerequisites

- Python 3.x
- Google Chrome
- ChromeDriver (must match your Chrome version)
- Install required Python package:

```bash
pip install selenium
```


## Task 1: Filter and Add to Cart

1. Login to the site
2. Sort products by `Price (low to high)`
3. Add the **first (cheapest)** product to the cart
4. Verify:
   - Product name
   - Price
   - Quantity = 1


## Task 2: Extract by Header

1. Sort products by `Name (Z to A)`
2. Extract and print the **first 3** product names and their prices



## How to Run

Save each task in a Python file and execute:

```bash
python task1_add_to_cart.py
python task2_extract_sorted_items.py
```

---

## Test DATA

Use the following standard test credentials:

- **Username:** `standard_user`
- **Password:** `secret_sauce`

---

