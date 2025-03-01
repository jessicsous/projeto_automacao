from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

user = os.getenv('USER')
password = os.getenv('PASS')
url = 'www.Booking.com.br'

def driver():
    caminho_driver = os.getcwd() + '/chromedriver'
    service = Service(caminho_driver)
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver