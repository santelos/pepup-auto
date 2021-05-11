from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def find_element_by_id_safe(driver, id: str):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, id))
    )

def find_element_by_name_safe(driver, name: str):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, name))
    )