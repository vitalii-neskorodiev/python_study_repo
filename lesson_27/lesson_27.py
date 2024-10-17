from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class NovaPoshtaTracker:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_parcel_status(self, tracking_number):
        try:
            self.driver.get("https://tracking.novaposhta.ua/#/uk")

            input_field = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#en"))
            )
            input_field.clear()
            input_field.send_keys(tracking_number)

            search_button = self.driver.find_element(By.CSS_SELECTOR, "#np-number-input-desktop-btn-search-en")
            search_button.click()

            status_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#chat > header > div.header__parcel-dynamic-status.px-4.d-flex.align-center > div.flex-grow-1 > div.header__status-text"))
            )

            parcel_status = status_element.text
            return parcel_status

        finally:
            self.driver.quit()


def run_parcel_status_check(tracking_number, expected_status):
    tracker = NovaPoshtaTracker()
    actual_status = tracker.get_parcel_status(tracking_number)

    assert actual_status == expected_status, f"Expected '{expected_status}', but got '{actual_status}'"
    print(f"Test passed: '{actual_status}' matches the expected status.")


run_parcel_status_check("20451000597264", "Отримана")
