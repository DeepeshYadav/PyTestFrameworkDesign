import pytest
from .initiate_driver import *
from .function_lib import *
from .test_data import *
import time
from logging import debug


def test_book_flight(test_setup_teardown):
    driver.find_element_by_id("gosuggest_inputSrc").send_keys("Pune")
    time.sleep(1)
    source_elems = driver.find_elements_by_xpath('//ul[contains(@id, "react-autosuggest")]//li')
    try:
        for elem in source_elems:
            sr_data = str(elem.text).split("\n")[0]
            if sr_data == 'Pune, India(PNQ)':
                elem.click()
                break
            else:
                continue
        time.sleep(5)
        driver.find_element_by_id("gosuggest_inputDest").send_keys("Mumbai")
        dest_elems = driver.find_elements_by_xpath('//ul[contains(@id, "react-autosuggest")]//li')
        for elem in dest_elems:
            ds_data = str(elem.text).split("\n")[0]
            if ds_data == 'Mumbai, India(BOM)':
                elem.click()
                break
            else:
                continue
    except:
        print("There is some exception")

def test_select_dates(test_setup_teardown):
        time.sleep(2)
        driver.find_element_by_id("departureCalendar").click()
        driver.find_element_by_id("fare_20200520").click()
        time.sleep(2)

        driver.find_element_by_id("returnCalendar").click()
        driver.find_element_by_id("fare_20200525").click()
        time.sleep(2)

        driver.find_element_by_id("pax_link_common").click()
        time.sleep(2)

        driver.find_element_by_id("adultPaxBox").send_keys("2")
        driver.find_element_by_id("childPaxBox").send_keys("2")
        driver.find_element_by_id("infantPaxBox").send_keys("1")

        driver.find_element_by_id('gi_class').click()
        time.sleep(2)
        driver.find_element_by_xpath("//option[@value='B']").click()
        time.sleep(2)
        driver.find_element_by_id('gi_search_btn').click()
        time.sleep(5)


@pytest.mark.smoke
@pytest.mark.sanity
def  test_search_hotel_and_verify(test_setup_teardown):
    """ This test function will search hotels in specific city.
    :return:
    """
    driver.get(GOIBIBO_GO_URL)
    go_to_hotel_page(driver)
    search_hotel(driver, CITYNAME)
    select_checkin_checkout_date(driver, CHECK_IN_DATE, CHECK_OUT_DATE)
    select_guest_and_room(driver, ROOM, GUEST, CHILD)


@pytest.mark.alert
@pytest.mark.sanity
def test_alert_functionality(test_setup_teardown):
    driver.get(ALERT_WEB_URL)
    accept_msg = handle_alert_box(driver)
    assert accept_msg == ALERT_CONFIRMATION_MSG


@pytest.mark.alert2
@pytest.mark.sanity
def test_confirm_box_functionality(test_setup_teardown):
    driver.get(ALERT_WEB_URL)
    accept_msg = handle_confirm_box(driver, accept=ACCEPT_CONFIRM)
    if ACCEPT_CONFIRM:
        assert accept_msg == CONFIRM_OK_MSG
    else:
        assert accept_msg == CONFIRM_CANCEL_MSG


@pytest.mark.alert3
def test_prompt_box_functionality(test_setup_teardown):
    driver.get(ALERT_WEB_URL)
    accept_msg = handle_prompt_box(driver, input=INPUT_NAME)
    if INPUT_NAME:
        assert accept_msg == f"Hello {INPUT_NAME}! How are you today?"
    else:
        print("Prompt Cancelled")







