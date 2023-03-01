import pytest
import allure

from pages.main_page import MainPage
from pages.main_page import LOCATOR_ORDER_FORM_METRO_KRASNOSELSKAYA, LOCATOR_ORDER_FORM_METRO_SOKOLNIKI, \
    LOCATOR_ORDER_FORM_METRO_KOMSOMOLSKAYA, LOCATOR_ORDER_FORM_METRO_KRASNYE_BOROTA, \
    LOCATOR_ORDER_FORM_DATE_FIRST_MARCH, LOCATOR_ORDER_FORM_DATE_SECOND_MARCH, LOCATOR_ORDER_FORM_DATE_THIRD_MARCH, \
    LOCATOR_TOP_ORDER_BUTTON, LOCATOR_BOTTOM_ORDER_BUTTON, LOCATOR_ORDER_FORM_RENT_TWO_DAYS, \
    LOCATOR_ORDER_FORM_RENT_THREE_DAYS, LOCATOR_ORDER_FORM_RENT_FOUR_DAYS, LOCATOR_ORDER_FORM_SCOOTER_COLOR_GRAY, \
    LOCATOR_ORDER_FORM_SCOOTER_COLOR_BLACK


@allure.title("Создание заказа")
@pytest.mark.parametrize(
    'order_button, name, lastname, address, metro, phone, data, quantity_days, scooter_color, comment',
    [
        [LOCATOR_TOP_ORDER_BUTTON, "Анна", "Николенко", "Москва, Озерная, 15", LOCATOR_ORDER_FORM_METRO_SOKOLNIKI,
         "+79500116161", LOCATOR_ORDER_FORM_DATE_FIRST_MARCH, LOCATOR_ORDER_FORM_RENT_TWO_DAYS,
         LOCATOR_ORDER_FORM_SCOOTER_COLOR_GRAY, "Буду дома после 18:00"],
        [LOCATOR_TOP_ORDER_BUTTON, "Мия", "Ушастая", "Москва, Дубовая аллея, 51", LOCATOR_ORDER_FORM_METRO_KOMSOMOLSKAYA,
         "+79500118834", LOCATOR_ORDER_FORM_DATE_SECOND_MARCH, LOCATOR_ORDER_FORM_RENT_THREE_DAYS,
         LOCATOR_ORDER_FORM_SCOOTER_COLOR_BLACK, "Буду дома до 12:00"],
        [LOCATOR_BOTTOM_ORDER_BUTTON, "Нина", "Лисичкина", "Москва, Речная, 25", LOCATOR_ORDER_FORM_METRO_KRASNOSELSKAYA,
         "+79965312983", LOCATOR_ORDER_FORM_DATE_FIRST_MARCH, LOCATOR_ORDER_FORM_RENT_FOUR_DAYS,
         LOCATOR_ORDER_FORM_SCOOTER_COLOR_GRAY, "Буду дома после 21:00"],
        [LOCATOR_BOTTOM_ORDER_BUTTON, "Соня", "Солнцева", "Москва, Озерная, 15", LOCATOR_ORDER_FORM_METRO_KRASNYE_BOROTA,
         "+79057895423", LOCATOR_ORDER_FORM_DATE_THIRD_MARCH, LOCATOR_ORDER_FORM_RENT_THREE_DAYS,
         LOCATOR_ORDER_FORM_SCOOTER_COLOR_BLACK, "Позвоните перед выездом"]
    ]
)
def test_create_order(browser, order_button, name, lastname, address, metro, phone, data, quantity_days, scooter_color,
                      comment):
    main_page = MainPage(browser)
    main_page.go_to_site()
    main_page.accept_cookies()
    main_page.order_button_click(order_button)
    main_page.order_form_enter_name(name)
    main_page.order_form_enter_lastname(lastname)
    main_page.order_form_enter_address(address)
    main_page.order_form_click_metro_station_field()
    main_page.order_form_choose_metro(metro)
    main_page.order_form_enter_phone(phone)
    main_page.order_form_click_dalee()
    main_page.order_form_calendar_field_click()
    main_page.order_form_date_click(data)
    main_page.order_form_rental_period_field_click()
    main_page.order_form_rental_period_quantity_days_click(quantity_days)
    main_page.order_form_scooter_color_click(scooter_color)
    main_page.order_form_comment_enter(comment)
    main_page.order_form_bottom_order_button_click()
    main_page.window_do_you_want_to_create_order_click_yes()
    assert main_page.window_your_order_created_is_visible()
