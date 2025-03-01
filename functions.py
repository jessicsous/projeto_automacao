from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from const import url, user, password

def acessar_site(driver):
    try:
        driver.get(url)

    except Exception as e:
        print(f"acessa_site function: {str(e)}")
        return False    

# def login(driver,ID,info,SLEEP):
#     try:
#         WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "")).send_Keys(user))
#         WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, "")).send_keys(password))
#         webDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, ""))).click()
#     except Exception as e:
#         print(f"login function: {str(e)}")
#         return False