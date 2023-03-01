from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

LOCATOR_LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")
LOCATOR_LOGO_YANDEX = (By.XPATH, "//a[@href='//yandex.ru']")


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://qa-scooter.praktikum-services.ru/'

    def go_to_site(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator),
                                                      message=f"Element is NOT VISIBILITY {locator}")

    def logo_scooter_click(self):
        return self.find_element(LOCATOR_LOGO_SCOOTER).click()

    def logo_yandex_click(self):
        return self.find_element(LOCATOR_LOGO_YANDEX).click()
