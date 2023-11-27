import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pyautogui

print("********** Welcome to Travel Planner **********")

destination = "Mumbai"
location = "Delhi"


class GoogleMaps:
    def __init__(self):
        options = Options()
        options.add_experimental_option('detach', True)
        obj = Service()
        self.driver = webdriver.Chrome(options=options, service=obj)
        self.driver.get("https://www.google.com/maps")
        self.driver.implicitly_wait(5)

    def search_place(self, destination):
        self.driver.find_element(By.XPATH, "//input[@jslog=11886]").send_keys(destination)
        self.driver.find_element(By.ID, "searchbox-searchbutton").click()

    def maximize_window(self):
        self.driver.maximize_window()

    def directions(self, location):
        self.driver.find_element(By.CLASS_NAME, "Cw1rxd.google-symbols.G47vBd").click()
        time.sleep(4)
        search_input = self.driver.find_element(By.XPATH, "//div[@class='sbib_b']//input")
        search_input.clear()
        search_input.send_keys(location)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='mL3xi']").click()
        time.sleep(3)

    def close(self):
        self.driver.quit()


class Details:
    def __init__(self, driver):
        self.time_text = ""
        self.duration_element_text = ""
        self.driver = driver
        self.train_name_text = ""


    def get_details(self):
        try:
            time_element = self.driver.find_element(By.CLASS_NAME, "VuCHmb.fontHeadlineSmall")
            self.time_text = time_element.text
            print("Time:", self.time_text)

            train_name_element = self.driver.find_element(By.XPATH, "//div[@class='CMnFh']")
            self.train_name_text = train_name_element.text
            print("Train Name:", self.train_name_text)

            duration_element = self.driver.find_element(By.XPATH, "//div[@class='XdKEzd']")
            self.duration_element_text = duration_element.text
            print("Duration:", self.duration_element_text)

            time.sleep(3)
            self.driver.save_screenshot("screenshot.png")

        except Exception as e:
            print(f"An error occurred: {e}")


# Example of how to use the classes
google_maps = GoogleMaps()

google_maps.search_place(destination)
google_maps.maximize_window()
google_maps.directions(location)

details_instance = Details(google_maps.driver)
details_instance.get_details()

google_maps.close()

time.sleep(2)

x = input("Do you want to send these details ? ").upper()
if x == 'YES':
    print('Great ! We will use proton to send an e-mail. Please create a new account if you do not have one.')
    username = input("Enter your username (CASE SENSITIVE): ")
    password = input("Enter your password (CASE SENSITIVE): ")
    recipient = input('Enter the recipient email address')

    class Email:
        def __init__(self):
            options = Options()
            options.add_experimental_option('detach', True)
            obj = Service()
            self.driver = webdriver.Chrome(options=options, service=obj)
            self.driver.get("https://account.proton.me/login")
            self.driver.maximize_window()
            time.sleep(6)

        def login(self, username, password):
            self.driver.find_element(By.ID, "username").send_keys(username)
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
            self.driver.find_element(By.XPATH, "//button[@class='button w-full button-large button-solid-norm mt-6']").click()
            time.sleep(20)

        def compose(self,recipient,train_name_text,time_text,duration_element_text):
            self.driver.find_element(By.XPATH,"//button[@aria-describedby='tooltip-7']").click()
            time.sleep(3)
            self.driver.find_element(By.XPATH,"//input[@placeholder='Email address']").send_keys(recipient)
            self.driver.find_element(By.XPATH,"//input[@placeholder='Subject']").send_keys('Travel Planner')
            time.sleep(2)
            iframe = self.driver.find_element(By.XPATH, "//iframe[@class='w100 h100 flex-item-fluid']")
            self.driver.switch_to.frame(iframe)
            email_body = self.driver.find_element(By.XPATH,"//div[@id='rooster-editor']")
            email_body.clear()
            email_body.send_keys('Hello,')
            email_body.send_keys('\nPlease look at the following details:- ')
            email_body.send_keys(f'\nTrain Name: {train_name_text}')
            email_body.send_keys(f'\nTrain Time: {time_text}')
            email_body.send_keys(f'\nDuration: {duration_element_text}')
            email_body.send_keys('\nThank you, ')
            email_body.send_keys('\nRahul Gera ')
            time.sleep(4)
            self.driver.switch_to.default_content()

            file_path = r'C:\Users\HP G5\PycharmProjects\pythonProject1\screenshot.png'
            self.driver.find_element(By.XPATH, "//label[@class='button button-for-icon button-ghost-weak inline-block text-center inline-flex']").click()
            time.sleep(2)

            pyautogui.write(file_path)
            pyautogui.press('enter')
            time.sleep(4)
            inline_button = self.driver.find_element(By.XPATH, "//button[@data-testid='composer:insert-image-inline']")
            inline_button.click()
            time.sleep(8)
            self.driver.find_element(By.XPATH, "//button[@class='button button-group-item button-solid-norm composer-send-button']").click()
            time.sleep(5)
            self.driver.close()


            print('********** Thank you for using Travel Planner **********')


    email_instance = Email()
    email_instance.login(username, password)
    email_instance.compose(recipient, details_instance.train_name_text,details_instance.time_text,details_instance.duration_element_text)

else:
    print('********** Thank you for using Travel Planner **********')

