from functions import *
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = driver()

    acessar_site(driver,ID,info,SLEEP)

    login(driver,ID,info,SLEEP)

except Exception as e:
    print(e)    