import os
from selenium import webdriver

def logIn(driver):  
    emailElem = findElementByIdSafe(driver, "sender-email")
    passElem = findElementByIdSafe(driver, "user-pass")
    
    emailElem.send_keys(os.getenv('USER_EMAIL'))
    passElem.send_keys(os.getenv('USER_EMAIL'))

    submitElem = findElementBynameSafe(driver, "commit")
    submitElem.click()


def findElementByIdSafe(driver, id: str):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id"))
    )

def findElementBynameSafe(driver, name: str):
    return WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )

driver = selenium.Firefox()
diver.get("https://pepup.life/users/sign_in")

logIn(driver)
