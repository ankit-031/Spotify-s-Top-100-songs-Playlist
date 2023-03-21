# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://www.google.com")
chromepath = "/Users/ankitparekh/Documents/chromedriver"
driver = webdriver.Chrome(chromepath)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
elements = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

print(elements.text)

