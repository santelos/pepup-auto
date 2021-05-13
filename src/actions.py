import logging
import os
from utils import find_element_by_id_safe, find_element_by_css_safe, find_element_by_name_safe

logging.getLogger().setLevel(logging.INFO)

def log_in(driver):
    driver.get("https://pepup.life/users/sign_in")
    email_elem = find_element_by_id_safe(driver, "sender-email")
    pass_elem = find_element_by_id_safe(driver, "user-pass")

    email_elem.send_keys(os.getenv('USER_EMAIL'))
    pass_elem.send_keys(os.getenv('USER_PASS'))

    submit_elem = find_element_by_name_safe(driver, "commit")
    submit_elem.click()

def input_temp(driver, temp: str):
    driver.get("https://pepup.life/daily_records/diary")

    temp_elem = find_element_by_css_safe(driver, ".sc-1ejhwgd-7.kGMvLc")[0]
    temp_elem.click()
    driver.implicitly_wait(2)
    temp_input_element = find_element_by_css_safe(driver, ".sc-9jpzzc-3.eZoVle")[0]
    temp_input_element.send_keys(temp)
    temp_input_submit = find_element_by_css_safe(driver, ".sc-1nyioy8-2.gdKtya")[0]
    temp_input_submit.click()

    check_element = find_element_by_css_safe(driver, ".sc-1ejhwgd-9.kelHZY")[0]
    if check_element.text != temp:
        raise RuntimeError(f"Temp value input error. Sould be [{temp}], but found [{check_element.text}]")
    logging.info(f"Temp finished. Value: [{check_element.text}]")

def input_weight(driver, weight: str):
    driver.get("https://pepup.life/daily_records/diary")
    
    weight_elem = find_element_by_css_safe(driver, ".sc-1ejhwgd-7.kGMvLc")[1]
    weight_elem.click()
    driver.implicitly_wait(2)
    weight_input_element = find_element_by_css_safe(driver, ".sc-9jpzzc-3.eZoVle")[0]
    weight_input_element.send_keys(weight)
    weight_input_submit = find_element_by_css_safe(driver, ".sc-1nyioy8-2.gdKtya")[0]
    weight_input_submit.click()
    
    check_element = find_element_by_css_safe(driver, ".sc-1ejhwgd-9.kelHZY")[1]
    if check_element.text != weight:
        raise RuntimeError(f"Weight value input error. Sould be [{weight}], but found [{check_element.text}]")
    logging.info(f"Weight finished. Value: [{check_element.text}]")

def input_steps(driver, steps: str):
    driver.get("https://pepup.life/daily_records/diary")
    
    steps_elem = find_element_by_css_safe(driver, ".sc-1ejhwgd-7.kGMvLc")[4]
    steps_elem.click()
    driver.implicitly_wait(2)
    steps_input_element = find_element_by_css_safe(driver, ".sc-9jpzzc-3.eZoVle")[0]
    steps_input_element.send_keys(steps)
    steps_input_submit = find_element_by_css_safe(driver, ".sc-1nyioy8-2.gdKtya")[0]
    steps_input_submit.click()

    check_element = find_element_by_css_safe(driver, ".sc-1ejhwgd-9.kelHZY")[2]
    if check_element.text != steps:
        raise RuntimeError(f"Steps value input error. Sould be [{steps}], but found [{check_element.text}]")
    logging.info(f"Steps finished. Value: [{check_element.text}]")
