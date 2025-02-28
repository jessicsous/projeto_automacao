from const import driver
from functions import acessar_site
from selenium.webdriver.support import expected_conditions as EC

try:
    driver_chrome = driver()

    acessar_site(driver_chrome)

    #login(driver,ID,info,SLEEP)

except Exception as e:
    print(e)    