from selenium import webdriver
import os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import platform


def driver():
    sistema = platform.system()

    if sistema == 'Linux':
        caminho_driver = os.getcwd() + '/chromedriver/linux/chromedriver'
    elif sistema == 'Windows':
        caminho_driver = os.getcwd() + '/chromedriver/windows/chromedriver'    
    
    service = Service(caminho_driver)
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--lang=pt-BR")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    return driver