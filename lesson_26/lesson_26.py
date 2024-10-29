from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

try:
    driver.get("http://localhost:8000/dz.html")

    driver.switch_to.frame("Frame1")
    input1 = driver.find_element(By.ID, "input1")
    input1.send_keys("Frame1_Secret")
    verify_button1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    verify_button1.click()

    alert1 = Alert(driver)
    assert alert1.text == "Верифікація пройшла успішно!"
    print("Перевірка у першому фреймі успішна.")
    alert1.accept()

    driver.switch_to.default_content()

    driver.switch_to.frame("Frame2")
    input2 = driver.find_element(By.ID, "input2")
    input2.send_keys("Frame2_Secret")
    verify_button2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
    verify_button2.click()

    alert2 = Alert(driver)
    assert alert2.text == "Верифікація пройшла успішно!"
    print("Перевірка у другому фреймі успішна.")
    alert2.accept()

finally:
    driver.quit()
