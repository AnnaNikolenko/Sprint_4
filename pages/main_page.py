from selenium.webdriver.common.by import By
from pages.base_page import BasePage

LOCATOR_COOKIE_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")

LOCATOR_HOW_MUCH_DOES_IT_COST = (By.XPATH, "//*[@id='accordion__heading-0']")
LOCATOR_I_WANT_A_COUPLE_OF_SCOOTERS = (By.XPATH, "//*[@id='accordion__heading-1']")
LOCATOR_HOW_RENT_TIME_IS_CALCULATED = (By.XPATH, "//*[@id='accordion__heading-2']")
LOCATOR_CAN_I_ORDER_SCOOTER_TODAY = (By.XPATH, "//*[@id='accordion__heading-3']")
LOCATOR_CAN_I_EXTEND_ORDER = (By.XPATH, "//*[@id='accordion__heading-4']")
LOCATOR_DO_YOU_BRING_CHARGING = (By.XPATH, "//*[@id='accordion__heading-5']")
LOCATOR_CAN_I_CANCEL_ORDER = (By.XPATH, "//*[@id='accordion__heading-6']")
LOCATOR_I_LIVE_FAR_WILL_YOU_BRING = (By.XPATH, "//*[@id='accordion__heading-7']")

LOCATOR_ANSWER_ABOUT_COST = (
    By.XPATH, "//p[contains(text(),'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')]")
LOCATOR_ANSWER_ABOUT_A_COUPLE_OF_SCOOTERS = (By.XPATH,
                                             "//p[contains(text(),'Пока что у нас так: один заказ — один самокат. "
                                             "Если хотите покататься с друзьями, можете просто сделать несколько "
                                             "заказов — один за другим.')]")
LOCATOR_ANSWER_HOW_RENT_TIME_IS_CALCULATED = (By.XPATH,
                                              "//p[contains(text(),'Допустим, вы оформляете заказ на 8 мая. Мы "
                                              "привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается "
                                              "с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 "
                                              "мая в 20:30, суточная аренда закончится 9 мая в 20:30.')]")
LOCATOR_ANSWER_ABOUT_ORDER_SCOOTER_TODAY = (
    By.XPATH, "//p[contains(text(),'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')]")
LOCATOR_ANSWER_ABOUT_EXTEND_ORDER = (By.XPATH,
                                     "//p[contains(text(),'Пока что нет! Но если что-то срочное — всегда можно "
                                     "позвонить в поддержку по красивому номеру 1010.')]")
LOCATOR_ANSWER_ABOUT_CHARGING = (By.XPATH,
                                 "//p[contains(text(),'Самокат приезжает к вам с полной зарядкой. Этого хватает на "
                                 "восемь суток — даже если будете кататься без передышек и во сне. Зарядка не "
                                 "понадобится.')]")
LOCATOR_ANSWER_ABOUT_CANCEL_ORDER = (By.XPATH,
                                     "//p[contains(text(),'Да, пока самокат не привезли. Штрафа не будет, "
                                     "объяснительной записки тоже не попросим. Все же свои.')]")
LOCATOR_ANSWER_I_LIVE_FAR_WILL_YOU_BRING = (
    By.XPATH, "//p[contains(text(),'Да, обязательно. Всем самокатов! И Москве, и Московской области.')]")

LOCATOR_TOP_ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[1]")
LOCATOR_BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[contains(text(), 'Заказать')])[2]")

LOCATOR_ORDER_FORM_NAME = (By.XPATH, "//input[@placeholder='* Имя']")
LOCATOR_ORDER_FORM_LASTNAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
LOCATOR_ORDER_FORM_ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
LOCATOR_ORDER_FORM_METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
LOCATOR_ORDER_FORM_METRO_SOKOLNIKI = (
    By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[4]/button/div[2]")
LOCATOR_ORDER_FORM_METRO_KRASNOSELSKAYA = (
    By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[5]/button/div[2]")
LOCATOR_ORDER_FORM_METRO_KOMSOMOLSKAYA = (
    By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[6]/button/div[2]")
LOCATOR_ORDER_FORM_METRO_KRASNYE_BOROTA = (
    By.XPATH, "//*[@id='root']/div/div[2]/div[2]/div[4]/div/div[2]/ul/li[7]/button/div[2]")
LOCATOR_ORDER_FORM_PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

LOCATOR_ORDER_FORM_DALEE_BUTTON = (By.XPATH, "//button[contains(text(),'Далее')]")

LOCATOR_ORDER_FORM_CALENDAR_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
LOCATOR_ORDER_FORM_DATE_FIRST_MARCH = (By.XPATH, "//div[@aria-label='Choose среда, 1-е марта 2023 г.']")
LOCATOR_ORDER_FORM_DATE_SECOND_MARCH = (By.XPATH, "//div[@aria-label='Choose четверг, 2-е марта 2023 г.']")
LOCATOR_ORDER_FORM_DATE_THIRD_MARCH = (By.XPATH, "//div[@aria-label='Choose пятница, 3-е марта 2023 г.']")
LOCATOR_ORDER_FORM_RENTAL_PERIOD = (By.XPATH, "//div[contains(text(),'* Срок аренды')]")
LOCATOR_ORDER_FORM_RENT_TWO_DAYS = (By.XPATH, "//div[contains(text(),'двое суток')]")
LOCATOR_ORDER_FORM_RENT_THREE_DAYS = (By.XPATH, "//div[contains(text(),'трое суток')]")
LOCATOR_ORDER_FORM_RENT_FOUR_DAYS = (By.XPATH, "//div[contains(text(),'четверо суток')]")
LOCATOR_ORDER_FORM_SCOOTER_COLOR_BLACK = (By.XPATH, "//input[@id='black']")
LOCATOR_ORDER_FORM_SCOOTER_COLOR_GRAY = (By.XPATH, "//input[@id='grey']")
LOCATOR_ORDER_FORM_COMMENT_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")

LOCATOR_ORDER_FORM_BOTTOM_ORDER_BUTTON = (By.XPATH, "(//button[contains(text(),'Заказать')])[2]")

LOCATOR_WINDOW_DO_YOU_WANT_TO_CREATE_ORDER_YES = (By.XPATH, "//button[contains(text(),'Да')]")
LOCATOR_WINDOW_YOUR_ORDER_IS_CREATED = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")


class MainPage(BasePage):
    def accept_cookies(self):
        return self.find_element(LOCATOR_COOKIE_BUTTON).click()

    def order_button_click(self, locator):
        return self.find_element(locator).click()

    def order_form_bottom_order_button_click(self):
        return self.find_element(LOCATOR_BOTTOM_ORDER_BUTTON).click()

    def order_form_enter_name(self, name):
        name_field = self.find_element(LOCATOR_ORDER_FORM_NAME)
        name_field.click()
        name_field.send_keys(name)
        return name_field

    def order_form_enter_lastname(self, lastname):
        last_name = self.find_element(LOCATOR_ORDER_FORM_LASTNAME)
        last_name.click()
        last_name.send_keys(lastname)
        return last_name

    def order_form_enter_address(self, address):
        my_address = self.find_element(LOCATOR_ORDER_FORM_ADDRESS)
        my_address.click()
        my_address.send_keys(address)
        return my_address

    def order_form_click_metro_station_field(self):
        self.find_element(LOCATOR_ORDER_FORM_METRO_STATION).click()

    def order_form_choose_metro_sokolniki(self):
        self.find_element(LOCATOR_ORDER_FORM_METRO_SOKOLNIKI).click()

    def order_form_choose_metro(self, locator):
        self.find_element(locator).click()

    def order_form_enter_phone(self, phone):
        my_phone = self.find_element(LOCATOR_ORDER_FORM_PHONE)
        my_phone.click()
        my_phone.send_keys(phone)
        return my_phone

    def order_form_click_dalee(self):
        self.find_element(LOCATOR_ORDER_FORM_DALEE_BUTTON).click()

    def order_form_calendar_field_click(self):
        self.find_element(LOCATOR_ORDER_FORM_CALENDAR_FIELD).click()

    def order_form_date_click(self, locator):
        self.find_element(locator).click()

    def order_form_rental_period_field_click(self):
        self.find_element(LOCATOR_ORDER_FORM_RENTAL_PERIOD).click()

    def order_form_rental_period_quantity_days_click(self, locator):
        self.find_element(locator).click()

    def order_form_rental_period_four_days_click(self):
        self.find_element(LOCATOR_ORDER_FORM_RENT_FOUR_DAYS).click()

    def order_form_scooter_color_click(self, locator):
        self.find_element(locator).click()

    def order_form_scooter_color_gray_click(self):
        self.find_element(LOCATOR_ORDER_FORM_SCOOTER_COLOR_GRAY).click()

    def order_form_comment_enter(self, comment):
        my_comment = self.find_element(LOCATOR_ORDER_FORM_COMMENT_FIELD)
        my_comment.click()
        my_comment.send_keys(comment)
        return my_comment

    def window_do_you_want_to_create_order_click_yes(self):
        return self.find_element(LOCATOR_WINDOW_DO_YOU_WANT_TO_CREATE_ORDER_YES).click()

    def window_your_order_created_is_visible(self):
        return self.find_element(LOCATOR_WINDOW_YOUR_ORDER_IS_CREATED)
