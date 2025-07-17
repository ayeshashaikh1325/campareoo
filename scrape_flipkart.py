from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def scrape_flipkart(product_name):
    chrome_options = Options()
    chrome_options.binary_location = r"C:\Users\newlo\chrome-win64\chrome.exe"  # Update with your Chrome path
    service = Service(r"C:\Users\newlo\chromedriver-win64\chromedriver.exe")  # Update with your ChromeDriver path
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.flipkart.com/")

    # Close the login popup if it appears
    try:
        close_popup = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), '✕')]"))
        )
        close_popup.click()
    except TimeoutException:
        print("No login popup found or popup did not appear.")

    # Perform the product search
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q"))
        )
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)
    except TimeoutException:
        print("Search box not found.")
        driver.quit()
        return []

    # Wait for the search results to load
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'cPHDOP')]"))
        )
    except TimeoutException:
        print("Search results did not load in time.")
        driver.quit()
        return []

    # Scrape the product names, prices, and URLs
    results = []
    try:
        # Scraping from grid format
        grid_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'cPHDOP')]")
        for product in grid_products:
            try:
                product_name = product.find_element(By.XPATH, ".//div[contains(@class, '_1sdMkc LFEi7Z')]").text
                product_price = product.find_element(By.XPATH, ".//div[contains(@class, 'Nx9bqj')]").text
                product_url = product.find_element(By.XPATH, ".//a[contains(@class, 'WKTcLC')]").get_attribute('href')
                results.append({"name": product_name, "price": product_price, "url": product_url})
            except Exception as e:
                print(f"Error extracting grid product details: {e}")

        # Scraping from list format (if applicable)
        list_products = driver.find_elements(By.XPATH, "//div[contains(@class, 'cPHDOP')]")
        for product in list_products:
            try:
                product_name = product.find_element(By.XPATH, ".//div[contains(@class, 'tUxRFH')]").text
                product_price = product.find_element(By.XPATH, ".//div[contains(@class, 'Nx9bqj _4b5DiR')]").text
                product_url = product.find_element(By.XPATH, ".//a[contains(@class, 'CGtC98')]").get_attribute('href')
                results.append({"name": product_name, "price": product_price, "url": product_url})
            except Exception as e:
                print(f"Error extracting list product details: {e}")

        print("Scraped Flipkart Results:", results)  # Debugging line
    except Exception as e:
        print("Error during scraping:", str(e))

    driver.quit()
    return results

