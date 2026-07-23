import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class login:
    def __init__(self, url: str):
        self.url = url
        self.driver = None

    def open(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(self.url)
        print(f"Opened: {self.url}")
        return self.driver

    def fill_email_and_submit(self, email: str):
        if self.driver is None:
            self.open()

        time.sleep(6)

        email_field = self.driver.find_element(By.XPATH, "//*[@type='email']")
        email_field.click()
        email_field.clear()
        email_field.send_keys(email)

        submit_button = self.driver.find_element(By.XPATH, "//*[@type='submit']")
        submit_button.click()

    def fill_password_and_sign_in(self, password: str):
        time.sleep(3)

        password_field = self.driver.find_element(By.XPATH, "//*[@type='password']")
        password_field.click()
        password_field.clear()
        password_field.send_keys(password)

        time.sleep(1)

        sign_button = self.driver.find_element(By.XPATH, "//*[@id='idSIButton9']")
        sign_button.click()

        time.sleep(1)

        yes_button = self.driver.find_element(By.XPATH, "//input[@value='Yes']")
        yes_button.click()

    def stay_open(self):
        if self.driver is None:
            self.open()
        input("Press Enter to close the browser...")
        self.close()

    def close(self):
        if self.driver is not None:
            self.driver.quit()
            self.driver = None
