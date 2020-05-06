from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

URL = "https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html"


def test_select_value():
    driver.get(URL)
    select_obj = Select(driver.find_element_by_id('select-demo'))
    select_obj.select_by_index(1)
    time.sleep(3)
    select_obj.select_by_value('Wednesday')
    time.sleep(3)
    select_obj.select_by_visible_text('Saturday')
    time.sleep(3)
    driver.close()