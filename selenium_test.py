import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Navigate to Alenka.ru
driver.get("https://alenka.ru")

time.sleep(3)  # Wait for the page to load

# Close any pop-ups if they appear
def close_popup():
    try:
        close_button = driver.find_element(By.XPATH, "//button[@class='close']")
        close_button.click()
    except:
        pass  # No pop-up found

close_popup()

# Search for a product (e.g., "chocolate")
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("шоколад" + Keys.RETURN)

time.sleep(3)  # Wait for search results to load

# Select a product from the search results
product = driver.find_element(By.XPATH, "//a[contains(@href, '/product/')]")
product.click()

time.sleep(3)  # Wait for the product page to load

# Add the product to the cart
add_to_cart_button = driver.find_element(By.XPATH, "//button[contains(text(), 'в корзину')]")
add_to_cart_button.click()

time.sleep(3)  # Wait for the product to be added to the cart

# Proceed to the cart page
cart_button = driver.find_element(By.XPATH, "//a[contains(@href, '/cart/')]")
cart_button.click()

time.sleep(3)  # Wait for the cart page to load

# Proceed to checkout
checkout_button = driver.find_element(By.XPATH, "//a[contains(@href, '/checkout/')]")
checkout_button.click()

time.sleep(3)  # Wait for the checkout page to load

# Fill in the checkout form (assuming test data)
name_field = driver.find_element(By.NAME, "name")
phone_field = driver.find_element(By.NAME, "phone")
email_field = driver.find_element(By.NAME, "email")
name_field.send_keys("Авт"Тестирование"
phone_field.send_keys("+79991234567")
email_field.send_keys"happygomakki@ya.ru"
# Add comments to the order
comments_field = driver.find_element(By.NAME, "comments")
comments_field.send_keys("Тестовый")

# Submit the order (this step is commented out to avoid placing an actual order)
# submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'оформить заказ')]")
# submit_button.click()

# Close the browser
driver.quit()
