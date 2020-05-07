from .test_data import *
import time
from logging import debug
from .initiate_driver import *
from .function_lib import *

def test_book_flight(test_setup_teardown):

    driver.find_element_by_id("gosuggest_inputSrc").send_keys(get_data_from_excel(EXCEL_PATH, 1, 2))
    time.sleep(1)
    source_elems = driver.find_elements_by_xpath('//ul[contains(@id, "react-autosuggest")]//li')
    try:
        for elem in source_elems:
            sr_data = str(elem.text).split("\n")[0]
            if sr_data == get_data_from_excel(EXCEL_PATH, 2, 2):
                elem.click()
                break
            else:
                continue
        time.sleep(5)
        driver.find_element_by_id("gosuggest_inputDest").send_keys(get_data_from_excel(EXCEL_PATH, 4, 2))
        dest_elems = driver.find_elements_by_xpath('//ul[contains(@id, "react-autosuggest")]//li')
        for elem in dest_elems:
            ds_data = str(elem.text).split("\n")[0]
            if ds_data == get_data_from_excel(EXCEL_PATH, 5, 2):
                elem.click()
                break
            else:
                continue
    except:
        print("There is some exception")