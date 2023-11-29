from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

browser.get("https://ecommerce-playground.lambdatest.io/index.php?route=account/register")

browser.implicitly_wait(0.5)

first_name = browser.find_element(By.ID, "input-firstname")
last_name = browser.find_element(By.ID, "input-lastname")
telephone = browser.find_element(By.ID, "input-telephone")
email = browser.find_element(By.ID, "input-email")
password = browser.find_element(By.ID, "input-password")
password_confirm = browser.find_element(By.ID, "input-confirm")
terms = browser.find_element(By.XPATH, value="//label[@for='input-agree']")
continue_button = browser.find_element(By.XPATH, value="//input[@value='Continue']")

first_name.send_keys("FFirstNameNew")
last_name.send_keys("LLastNameNew")
email.send_keys("sample-email1-new@data.com")
telephone.send_keys("+351999888889")
password.send_keys("12345679")
password_confirm.send_keys("12345679")
terms.click()
continue_button.click()

print(browser.title)
assert browser.title == "Your Account Has Been Created!"
