from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://qa-agent-admin-ui.alphaatlus.com/'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
    driver.maximize_window()
    driver.get(url)
    wait = WebDriverWait(driver, 20)
    print('TITLE:', driver.title)
    print('URL:', driver.current_url)

    locators = [
        (By.XPATH, "//*[@type='email']"),
        (By.XPATH, "//input"),
        (By.CSS_SELECTOR, "input"),
    ]

    for locator in locators:
        try:
            element = wait.until(EC.presence_of_element_located(locator))
            print('FOUND', locator, '->', element.get_attribute('outerHTML')[:800])
        except Exception as exc:
            print('MISS', locator, exc)

    print('--- PAGE SOURCE SNIPPET ---')
    print(driver.page_source[:6000])
finally:
    driver.quit()
