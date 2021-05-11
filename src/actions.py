import os
from utils import find_element_by_id_safe, find_element_by_name_safe

def log_in(driver):
    driver.get("https://pepup.life/users/sign_in")
    emailElem = find_element_by_id_safe(driver, "sender-email")
    passElem = find_element_by_id_safe(driver, "user-pass")

    emailElem.send_keys(os.getenv('USER_EMAIL'))
    passElem.send_keys(os.getenv('USER_PASS'))

    submitElem = find_element_by_name_safe(driver, "commit")
    submitElem.click()

def choose_daily_rec(driver):
    driver.get("https://pepup.life/daily_records/diary")
    