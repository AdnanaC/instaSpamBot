from selenium import webdriver
import os
import time
import configparser
import json
from selenium.common.exceptions import WebDriverException
import random

from explicit import waiter, XPATH, NAME, CSS
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import ui

# open comments file
# use data['name_of_array'] to refer the appropriate set of comments to be used

with open("1person_comments.json", "r") as read_file:
    data = json.load(read_file)


class InstaBot:

    def __init__(self, username, password):
        
        self.base_url = 'https://www.instagram.com'
        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login(username, password)

    # Login into a personal instagram account

    def login(self, username, password):
        self.driver.get('{}/accounts/login/'.format(self.base_url))

        time.sleep(1)

        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
        
    #navigate to saved posts

    def get_saved_posts(self, user):
        self.driver.get('{}/{}/saved'.format(self.base_url, user))
        time.sleep(3)

    def resolve_posts(self, comments):
        saved_posts = self.driver.find_elements_by_class_name('v1Nh3')
       
        saved_posts[0].click()
        time.sleep(random.randint(2, 3))

        for post in saved_posts:

            # Wait until the textarea is available

            while(1 == 1):
                try:
                    commentSection = ui.WebDriverWait(self.driver, 10).until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
                    self.driver.execute_script("arguments[0].scrollIntoView(true);", commentSection)
                    break
                except Exception:
                    time.sleep(random.randint(3,5))

            for comment in comments:

                # Check if previous comment is posted using the disable attribute
                # of the post button. Press the button while it's enabled
                postButton = self.driver.find_element_by_xpath( "//*[text()='Post']")

                while(not postButton.get_attribute("disabled")):
                    print(postButton.is_enabled())
                    try:
                         postButton = ui.WebDriverWait(self.driver, 10).until(
                             EC.element_to_be_clickable((By.XPATH, "//*[text()='Post']")))
                         postButton.click()
                         time.sleep(random.randint(4,10))
                    except Exception:
                         time.sleep(random.randint(5,7))

                #Wait until the textarea is available and insert comment
                while(1 == 1):
                    try:
                        commentSection = ui.WebDriverWait(self.driver, 10).until(
                            EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
                        commentSection.send_keys(comment)
                        time.sleep(random.randint(3,5))
                        break
                    except Exception:
                        time.sleep(random.randint(4,8))

                #Wait until the post button is available and click it once
                while(1 == 1):
                    try:
                         postButton = ui.WebDriverWait(self.driver, 10).until(
                             EC.element_to_be_clickable((By.XPATH, "//*[text()='Post']")))
                         postButton.click()
                         time.sleep(random.randint(3,5))
                         break
                    except Exception:
                        time.sleep(random.randint(4,7))
        
            self.driver.find_element_by_class_name("_65Bje").click()   
            time.sleep(1)
    
def spambot(username, password, comments):
    ig_bot = InstaBot(username, password)
    time.sleep(3)

    ig_bot.get_saved_posts(username)

    ig_bot.resolve_posts(comments)