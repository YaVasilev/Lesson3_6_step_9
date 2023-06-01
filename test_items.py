import time
import pytest
from selenium.webdriver.common.by import By



def test_choose_language(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    browser.get(link)
    time.sleep(2)

    btn_basket = browser.find_element(By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")

    assert btn_basket.is_displayed(), "Кнопка не найдена!"

