import logging
from actions import log_in
from pyvirtualdisplay import Display
from selenium.webdriver import Firefox

logging.getLogger().setLevel(logging.INFO)

display = Display(visible=0, size=(800, 600))
display.start()

driver = Firefox()

log_in(driver)

display.stop()
