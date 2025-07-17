from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


def scrape_amazon(product_name):
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Users\newlo\chrome-win64\chrome.exe"
    service = Service(r"C:\Users\newlo\chromedriver-win64\chromedriver.exe")
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.amazon.in/")

    # Search for the product
    search_box = driver.find_element("id", "twotabsearchtextbox")
    search_box.send_keys(product_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5)  # Allow time for results to load

    # Scrape product names, prices, and URLs for both list and grid views

    # Common XPaths to handle both List and Grid views
    product_elements = driver.find_elements("xpath", "//h2/a/span[contains(@class,'a-text-normal')]")
    price_elements = driver.find_elements("xpath", "//span[@class='a-price-whole']")
    url_elements = driver.find_elements("xpath", "//h2/a")  # Get the parent <a> tag for URLs

    # Fallback for grid view where product name and prices might be different in structure
    if not product_elements:
        product_elements = driver.find_elements("xpath", "//span[@class='a-size-base-plus a-color-base a-text-normal']")

    if not price_elements:
        price_elements = driver.find_elements("xpath", "//span[@class='a-price']/span[@class='a-offscreen']")

    if not url_elements:
        url_elements = driver.find_elements("xpath", "//a[@class='a-link-normal s-no-outline']")

    results = []
    for i in range(len(product_elements)):
        product_name = product_elements[i].text
        product_price = price_elements[i].text if i < len(price_elements) else "N/A"
        product_url = url_elements[i].get_attribute('href') if i < len(url_elements) else "N/A"

        results.append({
            "name": product_name,
            "price": product_price,
            "url": product_url
        })

    print("Scraped Amazon Results:", results)  # Debugging line
    driver.quit()
    return results

