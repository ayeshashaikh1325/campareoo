# 🛍️ Campareoo – E-commerce Price Comparison Tool

Campareoo is a Python-based web scraping project that compares product prices across multiple e-commerce platforms in real time. It helps users find the best deal by scraping product details from Amazon, Flipkart, Croma, and Snapdeal based on a search term.

---

## 🚀 Features

- 🔎 Takes product name input from user
- 🛒 Scrapes real-time product prices from:
  - Amazon
  - Flipkart
  - Croma
  - Snapdeal
- 📊 Displays name, price, and link to product page
- 🌐 Clean HTML output interface using Flask
- ⚡ Fast scraping only from user-selected websites (for optimization)

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Selenium, BeautifulSoup (BS4), Requests, Flask  
- **Web Automation:** ChromeDriver  

---
## 💡 How It Works

1. User enters product name in a web form
2. User selects which websites to fetch prices from
3. Scripts scrape live product details using Selenium
4. Output is displayed in a styled HTML results page

---
📦 Example Output
Website	Product Name	Price	Link</br>
Amazon	Logitech Mouse M170	₹699	🔗 Link</br>
Flipkart	Logitech M170 Wireless	₹649	🔗 Link</br>
Croma	Logitech Mouse M170	₹799	🔗 Link</br>
Snapdeal	Logitech M170	₹670	🔗 Link</br>

---
🧠 Author
Ayesha Shaikh
📫 ayeshashaikhh84@gmail.com



