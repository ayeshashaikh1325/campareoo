from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def scrape_snapdeal(product_name):
    # Specify the path to Chrome and ChromeDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Users\newlo\chrome-win64\chrome.exe"
    service = Service(r"C:\Users\newlo\chromedriver-win64\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.snapdeal.com")

    try:
        # Wait for the search box to be present
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "inputValEnter"))
        )

        search_box.send_keys(product_name)
        search_button = driver.find_element(By.CLASS_NAME, "searchformButton")
        search_button.click()

        # Wait for results to load
        time.sleep(5)  # Adjust this sleep time as necessary

        # Find product elements
        products = driver.find_elements(By.CLASS_NAME, "product-tuple-listing")
        results = []

        for product in products:
            title = product.find_element(By.CLASS_NAME, "product-title").text
            price = product.find_element(By.CLASS_NAME, "product-price").text
            url = product.find_element(By.CLASS_NAME, "dp-widget-link").get_attribute("href")

            results.append({
                "name": title,
                "price": price,
                "url": url
            })

        return results

    except Exception as e:
        print(f"An error occurred: {e}")
        return []
    finally:
        driver.quit()



