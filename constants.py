from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import os

def driver():
    options = Options()
    options.add_argument('window-size=1280,720')
    driver = webdriver.Chrome(options=options)

URL = os.getenv('URL')
USER = os.gentenv('USER')
PASS = os.getenv('PASS')
