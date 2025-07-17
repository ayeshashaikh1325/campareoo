from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import Keys for keyboard actions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_croma(product_name):
    # Specify the path to Chrome and ChromeDriver
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = r"C:\Users\newlo\chrome-win64\chrome.exe"
    service = Service(r"C:\Users\newlo\chromedriver-win64\chromedriver.exe")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://www.croma.com")

    try:
        # Wait for the search box to be present and interactable
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchV2"))
        )

        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)  # Simulate pressing Enter

        # Wait for results to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "li.product-item"))
        )

        # Find product elements
        products = driver.find_elements(By.CSS_SELECTOR, "li.product-item")
        results = []

        for product in products:
            title = product.find_element(By.CSS_SELECTOR, "h3.product-title").text
            price = product.find_element(By.CSS_SELECTOR, "span.plp-srp-new-amount").text
            url = product.find_element(By.CSS_SELECTOR, "a").get_attribute("href")

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


