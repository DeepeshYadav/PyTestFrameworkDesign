from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

driver = webdriver.Chrome(executable_path='D:\\chromedriver_win32\\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)
wait_time = WebDriverWait(driver, 20)

# Locators and Inputs

URL = "https://www.mysmartprice.com/mobile/apple-iphone-7-msp10208"


BEST_PRICE_CSS = "span[class='prdct-dtl__prc-val']"
GO_TO_FLIPKART_XPATH = "//div[@data-storename='flipkart']//a"
GO_TO_PAYTM_XPATH = "//div[@data-storename='paytmmall']//a"
GO_TO_AMAZON_XPATH = "//div[@data-storename='amazon']//a"
GO_TO_TATACLIQ_XPATH = "//div[@data-storename='tatacliq']//a"

FLIPKART_PRICE_XPATH = "(//div[contains(text(), '₹')])[1]"
AMAZON_PRICE_XPATH = "(//div[contains(text(), '₹')])[1]"
PAYTM_PRICE_XPATH = "//span[@class='_1V3w']"
TATACLIQ_PRICE_XPATH = "//h3[contains(text(), '₹')]"


@pytest.mark.parametrize("input, output", [(2, 10), (11, 50), (3, 15)])
def test_number_and_output(input, output):
    multi = input*5
    assert multi == output


#@pytest.mark.parametrize
@pytest.mark.price
def test_check_price_on_websites():
    driver.get(URL)
    best_price = driver.find_element_by_css_selector(BEST_PRICE_CSS).text
    driver.find_element_by_xpath(GO_TO_FLIPKART_XPATH).click()
    driver.switch_to.window(driver.window_handles[1])
    wait_time.until(EC.presence_of_element_located, (By.XPATH, FLIPKART_PRICE_XPATH))
    other_price = driver.find_element_by_xpath(FLIPKART_PRICE_XPATH).text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    assert best_price == other_price


@pytest.mark.price2
@pytest.mark.parametrize("WEBSITE, PRICE", [(GO_TO_FLIPKART_XPATH, FLIPKART_PRICE_XPATH), (GO_TO_PAYTM_XPATH, PAYTM_PRICE_XPATH), (GO_TO_TATACLIQ_XPATH, TATACLIQ_PRICE_XPATH)])
def test_check_price_on_websites(WEBSITE, PRICE):
    driver.get(URL)
    best_price = driver.find_element_by_css_selector(BEST_PRICE_CSS).text
    driver.find_element_by_xpath(WEBSITE).click()
    driver.switch_to.window(driver.window_handles[1])

    wait_time.until(EC.presence_of_element_located, (By.XPATH, PRICE))
    #other_price = driver.find_element_by_xpath(PRICE).text
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

    #assert best_price == other_price

