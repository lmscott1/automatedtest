from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import time
import os

load_dotenv()

username = os.environ.get("USERNAME")
password = os.environ.get("PASSWORD")



def signInDeets():

    signInUsernameInput = driver.find_element_by_xpath(
        "//input[@data-testid='SignInUsernameInput']")
    signInUsernameInput.send_keys(username)
    signInPasswordInput = driver.find_element_by_xpath(
        "//input[@data-testid='SignInPasswordInput']")
    signInPasswordInput.send_keys(password)
    signInPasswordInput.send_keys(Keys.RETURN)


def clickSurvey():

    driver.find_element_by_css_selector(
        'div[data-testid="NavigationlinksSurveys"]').click()
    # surveyButton.send_keys(Keys.RETURN)


PATH = "/Users/lukescott/Documents/Code/Python/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://csteam.hive.hr/sign-in")
print(driver.title)
time.sleep(5)


signInDeets()
time.sleep(10)
clickSurvey()

time.sleep(15)

driver.quit()
