from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time


service = Service(
    executable_path="/home/neko/Documents/Projects/TDD/chromedriver-linux64/chromedriver"
)
driver = webdriver.Chrome(service=service)
# service = Service(executable_path="/snap/bin/geckodriver")

# driver = webdriver.Firefox(service=service)

# driver.get('https://google.com')
driver.get("http://localhost:8000/")
# driver.get("https://127.0.0.1:8000/")

# driver.get('https://ya.ru')
time.sleep(10)
driver.quit()
assert 'Django' in driver.title
