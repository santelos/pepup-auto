import logging
from actions import input_steps, input_temp, input_weight, log_in
from pyvirtualdisplay import Display
from selenium.webdriver import Firefox

logging.getLogger().setLevel(logging.INFO)

display = Display(visible=0, size=(800, 600))
display.start()

driver = Firefox()

log_in(driver)
input_temp(driver, "36.7")
input_weight(driver, "75.0")
input_steps(driver, "8000")

display.stop()
