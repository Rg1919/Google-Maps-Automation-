import time

from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

x = input("Do you want to send these details to someone? ").upper()
if x == 'YES':
    username = input("Enter your username (CASE SENSITIVE): ")
    password = input("Enter your password (CASE SENSITIVE): ")
    time.sleep(4)
    class Email:
        def __init__(self):
            options = Options()
            options.add_experimental_option('detach', True)
            obj = Service()
            self.driver = webdriver.Chrome(options=options, service=obj)
            self.driver.get("https://account.proton.me/login")

        def login(self, username, password):
            self.driver.find_element(By.XPATH,"//input[class='input-element w-full']").send_keys(username)
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
            self.driver.find_element(By.XPATH, "//input[@aria-describedby='id-4']").click()

    email_instance = Email()
    email_instance.login(username, password)
