import allure
from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.main_page import LOCATOR_TOP_ORDER_BUTTON


@allure.title("Клик по логотипу Самокат")
def test_click_logo_scooter(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.order_button_click(LOCATOR_TOP_ORDER_BUTTON)
    base_page = BasePage(browser)
    base_page.logo_scooter_click()
    actual_result = browser.current_url
    expected_result = "https://qa-scooter.praktikum-services.ru/"
    assert actual_result == expected_result


@allure.title("Клик по логотипу Яндекс")
def test_click_logo_yandex(browser):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.order_button_click(LOCATOR_TOP_ORDER_BUTTON)
    base_page = BasePage(browser)
    base_page.logo_yandex_click()
    assert len(browser.window_handles) == 2
