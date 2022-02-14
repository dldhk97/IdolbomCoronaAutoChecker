from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def explicit_wait(driver, xpath):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located\
	                ((By.XPATH, xpath)))
    except Exception as e:
        pass