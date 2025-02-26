from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from constants import (
    URL
    USER
    PASS
)



def acessar_site(driver,ID,info,SLEEP):
    try:
        driver.get(URL)

    except Exception as e:
        print(f"login function: {str(e)}")
        return False    

def login(driver,ID,info,SLEEP):
    try:
        driver.get(f"www.Booking.com.br")
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "")).send_Keys(USER))
        WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "")).send_keys(PASS))
        webDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, ""))).click()
    except Exception as e:
        print(f"login function: {str(e)}")
        return False

    