import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Initialising driver

driver = webdriver.Chrome()

class Bot:
    def __init__(self, name, body_element):
        self.name = name
        self.controller = body_element

    def up(self):
        self.controller.send_keys(Keys.ARROW_UP)

    def down(self):
        self.controller.send_keys(Keys.ARROW_DOWN)

    def left(self):
        self.controller.send_keys(Keys.ARROW_LEFT)

    def right(self):
        self.controller.send_keys(Keys.ARROW_RIGHT)

    def run():
        pass

try:
    driver.get("https://tileman.io/")

    body_element = driver.find_element(By.TAG_NAME, "body")
    nickname_element = driver.find_element(By.ID, "nick")

    nickname = "tldr"

    # setting nickname to assert dominance

    nickname_element.clear()
    nickname_element.send_keys(nickname)

    # starting the game

    body_element.send_keys(Keys.ENTER)

    bot = Bot(nickname, body_element)

    # waiting 2 sec buffer (hopefully no ads idk)

    time.sleep(2)

    # control start from here

    bot.run()

    time.sleep(10)
finally:
    # quit driver to close

    driver.quit()